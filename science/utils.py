

def count_cag(seq):
    cag = "cag"
    prev = ""
    cag_count = 0
    max_cag_count = 0
    seq = seq.lower()
    for codon_start in range(0, len(seq), 3):
        codon = seq[codon_start:codon_start + 3]
        print(codon)
        if codon == cag:
            if prev == cag:
                cag_count += 1
                if cag_count > max_cag_count:
                    max_cag_count = cag_count
            else:
                prev = cag
                cag_count = 1
        else:
            cag_count = 0
            prev = ""
    return max_cag_count
            
            
        
