import numpy as np 
import matplotlib.pyplot  as plt 
from matplotlib import cm

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
        return (self.__signal_ensemble[:,i]*self.__signal_ensemble[:,j]).sum()/len(self.__signal_ensemble)
  
    
    def calc_time_ACF(self, sample_num):
        pass 

    def calc_total_average_power(self):
        pass 

    def plot_M_samples(self, M):
        samples = self.__signal_ensemble[np.random.randint(self.__signal_ensemble.shape[0],size=M)]
        fig, axs = plt.subplots(M)
        fig.suptitle(f"{M} Sample Functions of the given signal")
        for i in range(M):
            axs[i].plot(self.__time_vector, samples[i])
            axs[i].set_title(f"Realization {i}")

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
        ACF = np.zeros((len(self.__time_vector),len(self.__time_vector)))
        for i in range(len(self.__time_vector)):
            for j in range(len(self.__time_vector)):
                ACF[i,j] = self.calc_ACF(i,j)
        
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