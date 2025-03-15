def decodeBits(bits):
    # Remove leading and trailing zeros
    bits = bits.strip('0')
    
    if not bits:
        return ''
    
    # Find the transmission rate by determining the smallest sequence of 1s or 0s
    # First, split the string by '0' and '1' to get sequences
    ones_sequences = [len(seq) for seq in bits.split('0') if seq]
    zeros_sequences = [len(seq) for seq in bits.split('1') if seq]
    
    # If there are no sequences, return empty
    if (not ones_sequences) or (not zeros_sequences):
        return ''
    
    # Find the minimum length of sequences (this is likely our transmission rate)
    # For very simple cases, this might just be min(min_ones, min_zeros)
    # But we need to account for cases where the shortest sequence might not be the basic unit
    
    min_ones = min(ones_sequences) if ones_sequences else 0
    min_zeros = min(zeros_sequences) if zeros_sequences else 0
    
    # Determine the time unit (transmission rate)
    unit = min(min_ones, min_zeros) if min_zeros > 0 else min_ones

    # print(f"time unit: {unit}")
    
    # Now translate bits to Morse code
    morse = ''
    i = 0
    while i < len(bits):
        # Count consecutive 1s
        count_ones = 0
        while i < len(bits) and bits[i] == '1':
            count_ones += 1
            i += 1
        
        # Determine if it's a dot or dash
        if count_ones > 0:
            if count_ones // unit == 3:  # 3 units = dash
                morse += '-'
            else:  # assume it's a dot
                morse += '.'
        
        # print(f"before count zeros i is : {i}")

        # Count consecutive 0s
        count_zeros = 0
        while i < len(bits) and bits[i] == '0':
            count_zeros += 1
            i += 1
        
        # Determine spacing
        if count_zeros > 0:
            if count_zeros // unit == 7:  # 7 units = word space
                morse += '   '
            elif count_zeros // unit >= 3:  # 3 units = character space
                morse += ' '
            # 1 unit = pause between dots and dashes (no need to add anything)
    
    return morse

def decodeMorse(morse_code):
    MORSE_CODE = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
        '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
        '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+',
        '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$',
        '.--.-.': '@', '...---...': 'SOS'
    }
    
    morse_code = morse_code.strip()
    
    # Split by word (triple space)
    words = morse_code.split('   ')
    result = []
    
    for word in words:
        # Split by character (single space)
        chars = word.split(' ')
        decoded_word = ''
        
        for char in chars:
            if char:
                decoded_word += MORSE_CODE.get(char, '')
        
        if decoded_word:
            result.append(decoded_word)
    
    return ' '.join(result)



# bits = """1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"""

bits = str(input("Enter bits of message: "))

morse_string = decodeBits(bits)
print(f"""morse_string: {morse_string}""")

print("#"*20)

rslt = decodeMorse(morse_string)
print(f"""decode Morse String: {rslt}""")

