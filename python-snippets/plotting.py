# "new subplot discovery is leaving coders baffled try this today!!!" ~ Pratik
# sent by Pratik on April 8th 2018

import matplotlib.pyplot as plt

arr = [1, 2]
actual_radius = arr
mass_within_r = arr
sigma_within_r = arr
rad = arr
mass = arr
sigma = arr
fracdiff_mass = arr
fracdiff_sigma = arr

plt.subplot(2, 2, 1)
plt.plot(actual_radius, mass_within_r, c = 'b', label = "Pratik")                                                                                                          
plt.plot(rad, mass, c = 'k', label = "Grillo et al")
plt.xlim(10, 1000)
plt.ylim(1, 1000)
plt.xlabel("R (kpc)", fontsize=8)
plt.ylabel("M (<R)", fontsize=8)
plt.title("Mass plot", fontsize=10)
plt.legend(prop={'size':7}, loc=4)
plt.loglog()
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

plt.subplot(2, 2, 2)
plt.plot(actual_radius, sigma_within_r, c = 'b', label = "Pratik")                                                                                                                
plt.plot(rad, sigma, c = 'k', label = "Grillo et al")
plt.xlabel("R (kpc)", fontsize=8)
plt.ylabel("$\Sigma$ (<R)", fontsize=8)
plt.title("Surface Mass Density plot", fontsize=10)
plt.legend(prop={'size':7}, loc=4)
plt.loglog()
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)


plt.subplot(2, 2, 3)
plt.plot(rad, fracdiff_mass)
plt.ylim(-0.2, 0.35)
plt.xlabel("R (kpc)", fontsize=8)
plt.ylabel("(Model - Data)/Data", fontsize=8)
plt.title("Fractional difference in Mass", fontsize=10)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

plt.subplot(2, 2, 4)
plt.plot(rad, fracdiff_sigma)
plt.ylim(-0.2, 0.35)
plt.xlabel("R (kpc)", fontsize=8)
plt.ylabel("(Model - Data)/Data", fontsize=8)
plt.title("Fractional difference in SMD", fontsize=10)
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

plt.suptitle("Run 7: image plane, all members independent, slower than Run 5", fontsize=12)
plt.subplots_adjust(top=0.3)
plt.tight_layout(h_pad=0.2, rect=[0, 0.03, 1, 0.95])
plt.savefig("run7_massplots.pdf")
plt.show()
