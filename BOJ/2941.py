if __name__ == "__main__":
    change = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

    t_str = input()
    for sg in change:
        t_str = t_str.replace(sg, "0")
    print(len(t_str))
