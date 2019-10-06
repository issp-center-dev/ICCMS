import subprocess
import os

class calc_mag:
    def __init__(self, hphi_cond):
        self.input_param = {}
        self.path_hphi = hphi_cond["path_hphi"]
        self.input_path = hphi_cond["path_input_file"]
        self.input_param["model"] = "Spin"
        self.input_param["method"] = "CG"
        self.input_param["lattice"] = "chain"
        self.input_param["L"] = 12
        self.input_param["J0"] = 1.0
        self.input_param["J0'"] = 0.5
        self.input_param["J0''"] = 0.25
        self.input_param["exct"] = 2
        self.input_param["2Sz"] = 0
        self.energy_list = []

    def _make_input_file(self):
        with open(self.input_path, "w") as f:
            for key, item in self.input_param.items():
                f.write("{} = {}\n".format(key, item))

    def _change_input(self, input_dict):
        #input_dict = {J0: 1.0, J0': 0.5, J0'': 0.25)
        for key, value in input_dict.items():
            self.input_param[key] = value

    def _get_energy_from_hphi(self):
        energy_list = []
        if os.path.exists("./output/zvo_energy.dat"):
            str_output = "./output/zvo_energy.dat"
            with open(str_output, "r") as f:
                lines = f.readlines()
            for line in lines:
                line1 = line.split()
                if (line.find("Energy") != -1):
                    energy_list.append(float(line1[1]))
        return energy_list

    def get_energy_by_hphi(self, input_dict):
        self._change_input(input_dict)
        #update 2Sz
        L = self.input_param["L"]
        energy_list = []
        for sz in range(L//2 + 1):
            self.input_param["2Sz"] = 2*sz
            self._make_input_file()
            cmd = "{} -s {}".format(self.path_hphi, self.input_path)
            subprocess.call(cmd.split())
            energy = self._get_energy_from_hphi()
            energy_list.append((sz, energy[0]))
        self.energy_list = energy_list
        return energy_list

    def get_mag(self, sz_energy_list, H):
        energy_mag = []
        for sz_energy in sz_energy_list:
            energy_mag.append(sz_energy[1]-sz_energy[0]*H)
        min_index = energy_mag.index(min(energy_mag))
        return sz_energy_list[min_index][0]
