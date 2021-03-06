import numpy as np


class HMM:
    def __init__(self, t_probs, e_probs, pi, s_names, output):
        self.t_probs = t_probs
        self.e_probs = e_probs
        self.pi = pi
        self.s_names = s_names
        self.output = output

    def generate(self, length):
        initial_state = np.random.choice(self.s_names, p=self.pi)
        index = self.s_names.index(initial_state)

        x = np.array([])
        z = np.array([initial_state])
        for i in range(length):
            x_t = np.random.choice(self.output, p=self.e_probs[index])
            curr_state = np.random.choice(self.s_names, p=self.t_probs[index])
            index = self.s_names.index(curr_state)
            x = np.append(x, x_t)
            z = np.append(z, curr_state)

        return z, x

    def viterbi(self, observations):
        n_of_states = len(self.s_names)
        backtrace = []
        v = np.zeros((len(observations), n_of_states))
        for i, obs in enumerate(observations):
            index = self.output.index(obs)

            if i == 0:
                v_i = self.pi * self.e_probs[index]
                v[i] = v_i
                arg = v_i.argmax()
                backtrace.append(self.s_names[arg])
            else:
                v_i_options = np.zeros((n_of_states, n_of_states))
                for k in range(n_of_states):
                    option = self.e_probs[:, index] * self.t_probs[:, k] * v[i - 1]
                    v_i_options[k] = option
                v_i = v_i_options.max(axis=1)
                v[i] = np.array(v_i)
                arg = v_i.argmax()
                backtrace.append(self.s_names[arg])
        return backtrace

# Weather example
t_probs = np.array([[.6, .4], [.3, .7]])
e_probs = np.array([[.6, .4], [.9, .1]])
s_names = ['Sunny', 'Rainy']
output = ['Dirty', 'Clean']
pi = [.5, .5]
model = HMM(t_probs, e_probs, pi, s_names, output)
# print(model.generate(10))
# print(model.viterbi(['Dirty', 'Clean', 'Dirty', 'Dirty', 'Clean']))




# pos_model = HMM()