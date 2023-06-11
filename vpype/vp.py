import vpype




if __name__ == '__main__':
    path = 'vpype/input/0_#FF0000.svg'
    out = 'vpype/input/out_out.svg'
    a = vpype.read_svg(path, quantization=1)

    with open(out, 'w') as f:
        vpype.write_svg(f, a)

    print('Hello world!')

