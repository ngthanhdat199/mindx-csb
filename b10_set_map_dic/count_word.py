import subprocess

def word_freq_counter(text):
    word_freq = {}
    words = text.lower().split()
    words = map(lambda w: w.strip('.,!?;%"\'()[]{}'), words)
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
                
    return word_freq

result = subprocess.run([
    'curl', '-s', 'https://raw.githubusercontent.com/python/cpython/main/README.rst'
], capture_output=True, text=True)
content = result.stdout

print(word_freq_counter(content))