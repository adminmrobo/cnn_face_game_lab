# 손글씨 숫자(UCI, sklearn 내장) 오토인코더 64→64→2→64→64 를 numpy로 학습. 라벨은 학습에 쓰지 않는다.
import numpy as np, json
from sklearn.datasets import load_digits
D=load_digits(); X=D.data/16.0; y=D.target
rs=np.random.RandomState(7); idx=rs.permutation(len(X)); tr,te=idx[:1257],idx[1257:]
Xtr,Xte,yte=X[tr],X[te],y[te]
def init(i,o,r): return r.randn(i,o)*np.sqrt(1.0/i), np.zeros(o)
r=np.random.RandomState(3)
P={}
for n,(i,o) in zip(['1','2','3','4'],[(64,64),(64,2),(2,64),(64,64)]): P['W'+n],P['b'+n]=init(i,o,r)
def fwd(X,P):
    h1=np.tanh(X@P['W1']+P['b1']); z=h1@P['W2']+P['b2']; h3=np.tanh(z@P['W3']+P['b3']); o=1/(1+np.exp(-(h3@P['W4']+P['b4']))); return h1,z,h3,o
def enc(X,P): return np.tanh(X@P['W1']+P['b1'])@P['W2']+P['b2']
M={k:np.zeros_like(v) for k,v in P.items()}; V={k:np.zeros_like(v) for k,v in P.items()}
lr,b1,b2=0.003,0.9,0.999
STEPS=[0,10,30,60,120,250,500,1000,2000,3000]; snaps={}; losses=[]
for t in range(3001):
    h1,z,h3,o=fwd(Xtr,P); L=np.mean((o-Xtr)**2); losses.append(L)
    if t in STEPS: snaps[t]=(enc(Xte,P).copy(), float(np.mean((fwd(Xte,P)[3]-Xte)**2)), {k:P[k].copy() for k in ['W3','b3','W4','b4']})
    if t==3000: break
    n=len(Xtr); do=2*(o-Xtr)/(n*64)*o*(1-o); g={}
    g['W4']=h3.T@do; g['b4']=do.sum(0); dh3=do@P['W4'].T*(1-h3**2)
    g['W3']=z.T@dh3; g['b3']=dh3.sum(0); dz=dh3@P['W3'].T
    g['W2']=h1.T@dz; g['b2']=dz.sum(0); dh1=dz@P['W2'].T*(1-h1**2)
    g['W1']=Xtr.T@dh1; g['b1']=dh1.sum(0)
    for k in P:
        M[k]=b1*M[k]+(1-b1)*g[k]; V[k]=b2*V[k]+(1-b2)*g[k]**2
        P[k]-=lr*(M[k]/(1-b1**(t+1)))/(np.sqrt(V[k]/(1-b2**(t+1)))+1e-8)
def knn(Z,y,k=5):
    d=((Z[:,None,:]-Z[None,:,:])**2).sum(-1); np.fill_diagonal(d,1e18); nb=np.argsort(d,1)[:,:k]
    ok=0
    for i in range(len(Z)):
        c=np.bincount(y[nb[i]],minlength=10); ok+= (c.argmax()==y[i])   # 동점이면 작은 숫자 쪽
    return ok/len(Z)
mu=Xtr.mean(0); U,S,Vt=np.linalg.svd(Xtr-mu,full_matrices=False); Zp=(Xte-mu)@Vt[:2].T
Zae=snaps[3000][0]
print('loss train',losses[0],losses[-1],'test mse by step',{k:round(v[1],4) for k,v in snaps.items()})
print('kNN5 PCA',knn(Zp,yte),'AE',knn(Zae,yte),'by step',{k:round(knn(v[0],yte),3) for k,v in snaps.items()})
rec_p=((Xte-mu)@Vt[:2].T)@Vt[:2]+mu; print('PCA test mse',np.mean((rec_p-Xte)**2))
print('z range',Zae.min(0),Zae.max(0))
# 사람별(숫자별) kNN 적중
from collections import Counter
d=((Zae[:,None,:]-Zae[None,:,:])**2).sum(-1); np.fill_diagonal(d,1e18); nb=np.argsort(d,1)[:,:5]
hit=Counter(); tot=Counter()
for i in range(len(Zae)):
    c=np.bincount(yte[nb[i]],minlength=10); tot[yte[i]]+=1; hit[yte[i]]+= c.argmax()==yte[i]
print({k:round(hit[k]/tot[k],2) for k in range(10)})
np.savez('model.npz',**P,Zp=Zp,yte=yte,Xte=Xte,mu=mu,V2=Vt[:2],losses=np.array(losses),**{'snap%d'%k:v[0] for k,v in snaps.items()},**{'dec%d_%s'%(k,n):snaps[k][2][n] for k in STEPS for n in ['W3','b3','W4','b4']},snapmse=np.array([snaps[k][1] for k in STEPS]),steps=np.array(STEPS))
