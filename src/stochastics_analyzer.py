import numpy as np 
import matplotlib.pyplot  as plt 
from matplotlib import cm
from scipy.fft import fft 
class StochasticsAnalyzer():
    def __init__(self,time_vector, signal_ensemble) -> None:
        self.__time_vector = time_vector
        self.__signal_ensemble = signal_ensemble

    def calc_ensemble_mean(self)->np.array:
        return self.__signal_ensemble.sum(axis=0)/len(self.__signal_ensemble)

    def calc_time_mean(self, n):
        if n>=self.__signal_ensemble.shape[0]:
            raise ValueError("Invalid value for N")
            
        signal = self.__signal_ensemble[n]
        dt = self.__time_vector[1]-self.__time_vector[0]
        time_mean = np.sum(signal)*dt/(self.__time_vector[-1]-self.__time_vector[0])
        return time_mean

    def calc_ACF(self, i, j):
        return (self.__signal_ensemble[:,i]*self.__signal_ensemble[:,j]).sum()/(len(self.__signal_ensemble))
  
    def calc_full_stat_ACF(self):
        ACF = np.zeros((len(self.__time_vector),len(self.__time_vector)))
        for i in range(len(self.__time_vector)):
            for j in range(len(self.__time_vector)):
                ACF[i,j] = self.calc_ACF(i,j)
        
        return ACF
    
   

    def calc_total_average_power(self):
        x__2 = np.zeros(len(self.__signal_ensemble))
        dt = self.__time_vector[1]-self.__time_vector[0]
        
        for i in range(len(self.__signal_ensemble)):
            x__2[i] = ((self.__signal_ensemble[i])**2).sum()*dt 
        
        T = self.__time_vector[-1] - self.__time_vector[0]
        return np.round(x__2.sum()/(len(x__2)*T),3)
        
        

    def plot_M_samples(self, M):
        samples = self.__signal_ensemble[np.random.randint(self.__signal_ensemble.shape[0],size=M)]
        fig, axs = plt.subplots(M)
        fig.suptitle(f"{M} Sample Functions of the given signal")
        for i in range(M):
            axs[i].plot(self.__time_vector, samples[i])
            axs[i].set_title(f"Realization {i+1}")

        plt.show()

    def plot_ensemble_mean(self):
        plt.plot(self.__time_vector, self.calc_ensemble_mean())
        plt.title("Ensemble Mean Graph")
        plt.xlabel("Time (t)")
        plt.ylabel("Ensemble Mean")
        plt.grid()
        plt.show()
    

    

    def plot_time_mean(self):
        n = [i for i in range(len(self.__signal_ensemble))]
        means = [self.calc_time_mean(i) for i in range(len(self.__signal_ensemble))]
        plt.plot(n, means)
        plt.title("Time Mean Graph")
        plt.xlabel("N (Sample Index)")
        plt.ylabel("Time Mean")
        plt.grid()
        plt.show()
    
   

    def plot_stat_ACF(self):
        ACF = self.calc_full_stat_ACF() 
        X, Y = np.meshgrid(self.__time_vector, self.__time_vector)

        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        surf = ax.plot_surface(X, Y, ACF, cmap=cm.ocean)

        ax.set_title(f"Auto Correlation Function Graph")
        ax.set_xlabel("i")
        ax.set_ylabel("j") 
        ax.set_zlabel("R_x")
        fig.colorbar(surf, shrink=0.5, aspect=5)
        ax.view_init(45, 45)
        plt.show()
    
    def plot_PSD(self):
        n = len(self.__time_vector)
        fs = int(n/(self.__time_vector[-1]-self.__time_vector[0]))
        freqs = np.arange(-n/2,n/2,1)*(fs/n)
        PSD = np.zeros(len(freqs))
        T = self.__time_vector[-1] - self.__time_vector[0]
        for i in range(len(self.__signal_ensemble)):
            FT = np.fft.fft(self.__signal_ensemble[i])
            FT = np.fft.fftshift(FT)
            PSD = PSD + (abs(FT)**2)/(T*n)

        PSD = PSD/(len(self.__signal_ensemble))
        plt.xlabel("Frequency (rad/sec)")
        plt.ylabel("PSD")
        plt.plot(freqs, PSD)
        plt.show()
    
    def plot_time_ACF_for_sample(self, n):
        signal = self.__signal_ensemble[n]
        samples_difference = np.arange(0,len(self.__time_vector),1)
        taus = self.__time_vector
        time_ACF = np.zeros(len(taus))
        for delta in samples_difference:
            
            t1 = 0
            t2 = int(delta)
            dt = self.__time_vector[1] - self.__time_vector[0]
            
            print(time_ACF[delta])
            print(signal[t1])
            print(signal[t2])
            while t2<len(self.__time_vector):
                time_ACF[int(delta)] += signal[int(t1)]*signal[int(t2)]*dt/len(self.__time_vector) 
                t1+=dt 
                t2+=dt 
            
        plt.plot(taus, time_ACF)
        plt.xlabel("tau")
        plt.ylabel("Time ACF")
        plt.title("Time ACF vs Tau(time difference)")
        plt.grid()
        plt.show()
                

    
    def plot_full_time_ACF(self):
        pass 
