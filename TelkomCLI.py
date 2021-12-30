import sys

FUNCTIONLIST=[ #database
    {
        "Function":'help',
        "Alternate":'-h',
        "Description":"fungsi untuk menampilkan bantuan format: '-h' atau 'help'"
    },
    {
        "Function":'trans',
        "Alternate":'-t',
        "Description":"fungsi untuk mengubah file log menjadi txt atau json format: '{filepath} -t json'"
    },
    {
        "Function":'output',
        "Alternate":'-o',
        "Description":"fungsi untuk mengubah file log menjadi txt atau json format: '{filepath} -t json -o {outputpath}'"
    }
]
HElPFUNCTIONPOSITIONNUMBER = 0 #Help dictionary posituion order base on FUNCTIONLIST
TRANSPOSEFUNCTIONPOSITIONNUMBER = 1 #TRANSPOSE dictionary posituion order base on FUNCTIONLIST

def ReadArgs(Args, FunctionList):
    """
    check for input argument by comparing database into argument, return list of function call in argument
    """
    try:
        ReqFunction = []
        for Function in FunctionList:
            if Function['Alternate'] in str(Args).lower() or Function['Function'] in str(Args).lower():
                ReqFunction.append(Function['Function'])
            else:
                None
    except:
        print("Tidak ada input atau input salah, tulis help atau -h untuk mencari tau")
        exit()
    return ReqFunction

def Help(AllFunctionNames):
    """
    when argument input call, this function will show up
    """
    print(f'Fungsi Nama\tAlternative\tFungsi Deskripsi \n')
    for Function in AllFunctionNames:
        print(f'{Function["Function"]}\t\t{Function["Alternate"]}\t\t{Function["Description"]}')
    print("keterangan tambahan:")
    print("untuk format lebih detail mengikuti contoh di file pdf, jadi contoh dipdf bisa dilakukan juga disini")
    return None

def ConvertToJson(FilePath, FileOutPut = None):
    """
    function to convert to json by rewriting all line to new file
    """
    try:
        File = open(FilePath,"r")
        NewFileName = FilePath[:-4]
        NewFile = open(f'{NewFileName}.json', "w") if FileOutPut == None else open(FileOutPut,"w")
        for line in File:
            NewFile.writelines(f'{str(line)}')
        File.close()
        NewFile.close()
        print("proses selesai")
    except:
        print("something wrong")
        exit()
    return None

def ConvertToPlain(FilePath, FileOutPut = None):
    """
    function to convert to plain text by rewriting all line to new file
    """
    try:
        File = open(FilePath,"r")
        NewFileName = FilePath[:-3]
        NewFile = open(f'{NewFileName}.txt', "w") if FileOutPut == None else open(FileOutPut,"w")
        for line in File:
            NewFile.writelines(f'{str(line)}')
        File.close()
        NewFile.close()
        print("proses selesai")
    except:
        print("something wrong")
        exit()
    return None

def Transpose(Args):
    """
    function when only transpose in argument, will chose json or plain text convertion
    """
    try:
        FilePath =  Args[0]
        TransposeType = None if len(Args)<3 else str(Args[2]).lower()
        if TransposeType == "json":
            ConvertToJson(FilePath)
        else:
            ConvertToPlain(FilePath)
    except:
        print("Argumen yang dimasukkan tidak lengkap atau salah")
        exit()
    return None

def Output(Args):
    """
    function when there is output in argument, use same convert funtion with Transpose but with output path and also there is validation for the output path so the Transpose and expekted Output Path are the same 
    example: -t json but -o to .txt
    """
    try:
        FilePath =  Args[0]
        FileOutput = Args[-1]
        TransposeType = None if len(Args)<5 else str(Args[2]).lower()
        
        if TransposeType == 'json' and TransposeType != str(FileOutput[-4:]):
            raise ValueError("format transpose berbeda dengan otput path")
        elif TransposeType == 'txt' and TransposeType != str(FileOutput[-3:]):
            raise ValueError("format transpose berbeda dengan otput path")
        
        if TransposeType == "json":
            ConvertToJson(FilePath, FileOutput)
        else:
            ConvertToPlain(FilePath, FileOutput)
    except:
        print("format transpose berbeda dengan otput path atau Argumen yang dimasukkan tidak lengkap atau salah")
        exit()
    return None
    
def Exe(FunctionLists, Args, ListOfAllFunctionNames, HelpFunctionOrder, TransposeFunctionOrder):
    """
    function after ReadArgs to determine wich one suited for condition (only if els)
    """
    try:
        if len(FunctionLists)<2 and FunctionLists[0] == ListOfAllFunctionNames[HelpFunctionOrder]["Function"]:
            Help(ListOfAllFunctionNames)
        elif len(FunctionLists)<2 and FunctionLists[0] == ListOfAllFunctionNames[TransposeFunctionOrder]["Function"]:
            Transpose(Args)
        elif ListOfAllFunctionNames[HelpFunctionOrder]["Function"] not in FunctionLists:
            Output(Args)
        else:
            raise ValueError
    except:
        print("fungsi tidak terbaca atau kombinasi fungsi salah")
        exit()
    return None

if __name__ == "__main__":
    Args = []
    for Counter, Arg in enumerate(sys.argv):
        if Counter>0:
            Args.append(str(Arg))
    Functions = ReadArgs(Args, FUNCTIONLIST)
    Exe(Functions, Args, FUNCTIONLIST, HElPFUNCTIONPOSITIONNUMBER, TRANSPOSEFUNCTIONPOSITIONNUMBER)