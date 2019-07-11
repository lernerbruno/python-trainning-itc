import numpy as np


class HMM:
    def __init__(self, t_probs, e_probs, pi ,s_names, output):
        self.t_probs = t_probs
        self.e_probs = e_probs
        self.pi = pi
        self.states_names = s_names
        self.output = output

    def generate(self, length):
        initial_state = np.random.choice(self.states_names, p=self.pi)
        index = self.states_names.index(initial_state)

        x = np.array([])
        z = np.array([initial_state])
        for i in range(length):
            x_t = np.random.choice(self.output, p=self.e_probs[index])
            curr_state = np.random.choice(self.states_names, p=self.t_probs[index])
            index = self.states_names.index(curr_state)
            x = np.append(x, x_t)
            z = np.append(z, curr_state)

        return z, x


t_probs = np.array([[.6, .4], [.3, .7]])
e_probs = np.array([[.6, .4], [.9, .1]])
s_names = ['Sunny', 'Rainy']
output = ['Dirty', 'Clean']
pi = [.2, .8]
model = HMM(t_probs, e_probs, s_names, output)
print(model.generate(10))
