import numpy as np
import scipy.linalg as la

tx = np.array([1, np.exp(1j*np.pi*(np.cos(np.deg2rad(30))))+np.exp(1j*np.pi*(np.cos(np.deg2rad(45))))])

rx = np.array([[1 + np.exp(1j*2*np.pi*(np.cos(np.deg2rad(60))))], [1+np.exp(1j*2 *
              np.pi*(np.cos(np.deg2rad(30))))], [1+np.exp(1j*2*np.pi*(np.cos(np.deg2rad(120))))], [1+np.exp(1j*2*np.pi*(np.cos(np.deg2rad(210))))]])

print(tx)

print(rx)
        
rx.ndim

tx.ndim      
# H = rx @ tx.T 

# print(H)    
             
