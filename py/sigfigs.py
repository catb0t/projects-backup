def count_sig_figs(answer):
    '''This fucntion will count the sigfigs used in the answer of a user'''
    sig_fig_count = 0
    num_list = list(answer)

    for index in range(len(num_list)):
        try:
            fig = int(num_list[index])
            if fig != 0:
                sig_fig_count +=1
            elif check_zero_sig(index, num_list, sig_fig_count):
                sig_fig_count += 1
        except:
            continue
    return sig_fig_count

def check_zero_sig(index, num_list, sig_fig_count):
    '''Checks for significance in a zero from a list'''
    try:
        decimal = num_list.index('.')
        if index > decimal and sig_fig_count > 0:
            return True
    except:
        if index == 0:
            return False
        elif index == len(num_list):
            return False
        new_index = index+1

        if num_list[new_index] == '.' and sig_fig_count > 0:
            return True
        elif num_list[new_index] == '.' and sig_fig_count == 0:
            return False
        elif num_list[new_index] != '.' and sig_fig_count > 0:
            fig = int(num_list[new_index])
            if fig != 0:
                return True
            else:
                return check_zero_sig(new_index, num_list, sig_fig_count)
        elif num_list[new_index] != '.' and sig_fig_count == 0:
            fig = int(num_list[new_index])
            if fig != 0:
                return True
            else:
                return check_zero_sig(new_index, num_list, sig_fig_count)
        else:
            return False

def test():
    print(count_sig_figs('1')) # 1 sig fig
    print(count_sig_figs('10')) # 1 sig fig
    print(count_sig_figs('100')) # 1 sig fig
    print(count_sig_figs('1004')) # 4 sig figs
    print(count_sig_figs('10004')) # 5 sig figs
    print(count_sig_figs('105')) # 3 sig figs
    print(count_sig_figs('01')) # 1 sig fig
    print(count_sig_figs('1.2035')) # 5 sig figs
    print(count_sig_figs('001.09508')) # 6 sig figs
    print(count_sig_figs('0.00110')) # 3 sig figs

if __name__ == "__main__":
    test()