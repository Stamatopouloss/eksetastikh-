# 13.H υπηρεσία https://www.cloudflare.com/en-gb/leagueofentropy/ προσφέρει τυχαίους αριθμούς. Χρησιμοποιείστε αρχικά την διεύθυνση https://drand.cloudflare.com/public/latest για να πάρετε το τελευταίο randomness το οποίο θα το χωρίσετε σε δυάδες δεκαεξαδικών χαρακτήρων, και κάθε μια θα την μετρέψετε σε ακέραιο και θα την κάνετε modulo 80. Κρατείστε αυτούς τους 32 αριθμούς μοναδική φορά το καθένα και υπολογίστε πόσοι από αυτούς τους αριθμούς θα κληρονόντουσαν στην τελευταία κλήρωση του ΚΙΝΟ που θα βρείτε εδώ https://api.opap.gr/draws/v3.0/1100/last-result-and-active
import requests
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
randomness = data['randomness']

randomness_hex = []
for i in range(0,len(randomness),2):
    randomness_hex.append(randomness[i:i+2])

randomness_dec = [int(i, base=16)%80 for i in randomness_hex]
unique_nums = set(randomness_dec)

r = requests.get('https://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
winning = data['last']['winningNumbers']['list']

s = 0
print("The winning numbers would be:")
for num in unique_nums:
    if num in winning:
        s += 1
        print(num)
