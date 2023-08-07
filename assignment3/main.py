with open('input.txt', mode='r') as input_file:
    #Block for getting the no. of lines in input.txt
    no_of_lines = len(input_file.readlines())
    print(f"No. of lines in input.txt file is {no_of_lines}.")
    input_file.close()


with open('input.txt', mode='r') as input_file:
    # Block for getting the no. of words in input.txt
    data = input_file.read()
    updated_data = data.replace('.',' ')
    words = updated_data.split()
    print(f"No. of words in input.txt file is {len(words)}.")
    input_file.close()


with open('input.txt', mode='r') as input_file:
    # Block for writing the data of input.txt in output.txt(in reverse order)
    data = input_file.read()
    with open('output.txt', mode='r+') as output_file:
        output_file.write(data[::-1])
        print("We have successfully wrote the text of input.txt into output.txt in reverse order")
        '''
        In output.txt, the content will be:
        .sesoprup gnitset rof elif siht yfidom ot eerf leeF.dedeen sa tnetnoc eht etalupinaM.sesarhp ro sdrow cificeps rof hcraeS.sdrow ro senil fo rebmun eht tnuoC.elif siht no snoitarepo suoirav mrofrep nac uoY
        .elpmaxe na sa sevres enil hcaE.txet fo senil elpitlum sniatnoc tI.elif txet elpmas a si sihT
        '''

