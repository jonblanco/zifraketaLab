from collections import Counter
def deszifratu2():
    #mezua jarri eta letrak zenbatzen dira Counter-a erabiliz
    mezua="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
    letrak=Counter(mezua)
    print(letrak)
    #letrak banan banan aldatzen dira
    mezua=mezua.replace('X', 'e')
    mezua=mezua.replace('E', 'a')
    mezua = mezua.replace('T', 'l')
    mezua = mezua.replace('A', 'd')
    mezua = mezua.replace('R', 'c')
    mezua = mezua.replace('N', 's')
    mezua = mezua.replace('C', 'i')
    mezua = mezua.replace('J', 'n')
    mezua = mezua.replace('D', 'p')
    mezua = mezua.replace('Z', 'u')
    mezua = mezua.replace('P', 'm')
    mezua = mezua.replace('K', 'r')
    mezua = mezua.replace('I', 'o')
    mezua = mezua.replace('H', 't')
    mezua = mezua.replace('U', 'g')
    mezua = mezua.replace('S', 'q')
    mezua = mezua.replace('G', 'j')
    mezua = mezua.replace('F', 'x')
    mezua = mezua.replace('Q', 'b')
    mezua = mezua.replace('O', 'f')
    mezua = mezua.replace('M', 'h')
    mezua = mezua.replace('V', 'y')
    print(mezua)

deszifratu2()
