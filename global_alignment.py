import blosum as bl
import pandas as pd

matrix = bl.BLOSUM(50)

di = {}


def check(q, w):
    if str(first_subsequence[q]) == str(second_subsequence[w]):
        return first_subsequence[q]
    else:
        return matrix[str(first_subsequence[q] + second_subsequence[w])]


first_subsequence = "MQLLPEDDKMGSTMQESLSKRALESADAFGAMAGLMKVFQNMYNKEKNPNGIISLGVAENSLMHKELVDYYADKIKVTSYDLTYGAGPGGSPILREALASLYNRKFSPTFEVKPEHVYTAIGVSGVLDLLFHTIADEGDAILIGRPIYTGFAHDLYGRSKLKLVPVSLKDVDPMGPEAIKYYEKELQVQRNNGVKVRGIILCNPHNPLGKCYTPEVIKEYAKFCNSHQIHFISDEIYALSIYSTPSNTSATPFTSAFAVPGLREVISPHLVHVVYGMSKDFCANGLRMGCLISPWNDQIFLAAVVAVGLFQWPSSLPDIAWRTILNDHEFLDQFVIENQKKLGEHYQILVDWFEKHSIPYVAGSNAGFFIWTDLRRYLAKIKLPKGDDGKIPGGKTNIPGQPEGAQKRDKILWEKMIDGGVYVGSAEMFFGEEHGWYRFSFSTPREELELGLSRMEKVLKKVDEEAALEGLEGLNVNф"

second_subsequence = "MRTHTRGAPSVFFICLLCCVSAFITDENPEVMIPFTNANYDSHPMLYFSRKDVAELQLRAASSHEHIAARLTEAVHTMLTNPLEYLPPWDPKEYSARWNEIYGNNLGALAMFCVLYPENTEARDMAKDYMERMAAQPSWLVKDAPWDEVPLAHSLVGFATAYDFLYNYLSKTQQETFLEVIANASGYMYETSYRRGWGFQYLHNHQPTNCMALLTGSLILMNQGYLQEAYLWTKQVLSIMEKSLVLLREVTDGSLYEGVAYGSYTTRSLFQYMFLVQRHFDINHFGHPWLKQHFAFMYRTILPGFQRTVAIADSNYNWFYGPESQLVFLDKFVMRNGSGNWLADQIRRNRVVEGPGTPSKGQRWCTLHTEFLWYDASLKPVPPPDFGTPTLHYFEDWGVVTYGSALPAEINRSFLSFKSGKLGGRAIYDIVHRNKYKDWIKGWRNFNAGHEHPDQNSFTFAPNGVPFITEALYGPKYTYFNNVLMFSPAVSKSCFSPWEGQVTEDCSSKWSKYKHDLAASCQGRVIAADEKDGVVFIRGEGVGAYNPMLNLKHIQRNLILLHPQLLLLVDQIHLGEESPLETAASFFHNVDVPFEETVVDGVHGALIRQRDGLYKMYWMDDTGYSEKANFASVMYPRGYPYNGTNYVNVTMHLRSPITRAAYLFIGPSVDVQSFSIHGDPQRLDVFIATSEHAYATYLWTGENTGHSAFAQVIADHQKILFDQSSAIKSTAVPEVKDYAAIVEQNLQHFKPVFQLLEKQILSRVQNTASFRKTAERLLRFSDKRQTEEAIDRIFAISQQQRQQRGKSKKSRKAGKHYKFVDAVPDIFAQIEVNEKKIRQKAQVLAQREQPIDEDEEMKDLLDFADVTYEKHKNEGSVKGGFGQVRMVTSHNRAPSLSASYTRLFLILNIAIFFVMLAMQLTYFQRAQSLHGQRCLYAVLLIDSCVLLWLYSSCSQSQC"

# first_subsequence = input("Введите первую последовательность -> ")
# second_subsequence = input("Введите вторую последовательность -> ")
fine = int(input('Введите размер штрафа -> '))

# print(len(first_subsequence), len(second_subsequence)) # 478 and 958

pl = []
col = [0]
lin = [0]

for i in range(len(first_subsequence) + 1):
    pl.append([])
    if i < len(first_subsequence):
        col.append(first_subsequence[i])
    for j in range(len(second_subsequence) + 1):
        if i == j == 0:
            di[str(i) + str(j)] = 0
        elif i == 0 and j != 0:
            di[str(i) + str(j)] = di[str(i) + str(j - 1)] - fine
            lin.append(second_subsequence[j - 1])
        elif i != 0 and j == 0:
            di[str(i) + str(j)] = di[str(i - 1) + str(j)] - fine
        else:
            di[str(i) + str(j)] = max((di[str(i - 1) + str(j)] - fine), (di[str(i) + str(j - 1)] - fine),
                                      (di[str(i - 1) + str(j - 1)] + matrix[
                                          str(first_subsequence[i - 1] + second_subsequence[j - 1])]))
        pl[i].append(di[str(i) + str(j)])

df = pd.DataFrame(pl, index=col, columns= lin)

df.to_excel('./alignment.xlsx')

print()
print("Вес оптимального выравнивания: ", di[str(len(first_subsequence)) + str(len(second_subsequence))])
print()
print("Глобальное выравнивание изображено в файле 'alignment.xlsx'")
