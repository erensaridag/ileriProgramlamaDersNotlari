 # 4x4’lük 1–20 arasında rastgele matris:

def rastgele_matris():
    import numpy as np
    M = np.random.randint(1, 21, (4, 4))
    print(M)

rastgele_matris()