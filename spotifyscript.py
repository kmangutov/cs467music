import json
import requests as rq

OAuth = 'BQD7_lXq1b6LH1ldJYFIVELxWB1dYYHjtZsJRYyu3DoUDoJoSSEF2dqwnUzW6pxfWPbUTbWKsWC0kCFT-hxikfV34XCpa4Uakc5nnm-gDiY_LuG2waRC9jfhKSBhEbA2wDBRHCsQLvWLCu7pqt0BWTsaYU9rhv8'

input_file = 'songurls.txt'
output_file = 'data_temp.json'

def scale_tempo(tempo):
    value = (tempo/220)
    truncated = "%.3f" % value
    return float(truncated)


def parse_url(url):
    # Format:
    #https://play.spotify.com/track/uri
    return url[31:53]


def parse_data(name,dance,energy,speech,acou,instr,live,valen,tempo):
    result = \
    {
        'key':name,
        'values':
        [
            {
                'reason': 'danceability',
                'device': name,
                'value': dance
            },
            {
                'reason': 'energy',
                'device': name,
                'value': energy
            },
            {
                'reason': 'speechiness',
                'device': name,
                'value': speech
            },
            {
                'reason': 'acousticness',
                'device': name,
                'value': acou
            },
            {
                'reason': 'instrumentalness',
                'device': name,
                'value': instr
            },
            {
                'reason': 'liveness',
                'device': name,
                'value': live
            },
            {
                'reason': 'valence',
                'device': name,
                'value': valen
            },
            {
                'reason': 'tempo',
                'device': name,
                'value': tempo
            }
        ]
    }
    return result


def make_entry(uri):
    authorization = 'Bearer ' + OAuth
    headers = {
        'Accept': 'application/json',
        'Authorization': authorization,
    }
    response = rq.get('https://api.spotify.com/v1/audio-features/'+uri, headers=headers)
    if (response.status_code != 200):
        print('Get request failed...')
        exit(1)
    data = response.json()
    get_name = rq.get(data['track_href'])
    if (get_name.status_code != 200):
        print('Get request failed...')
        exit(1)
    name = get_name.json()['name']
    dance = data['danceability']
    energy = data['energy']
    speech = data['speechiness']
    acou = data['acousticness']
    instr = data['instrumentalness']
    live = data['liveness']
    valen = data['valence']
    tempo = scale_tempo(data['tempo'])
    parsed = parse_data(name, dance, energy,speech,acou,instr,live,valen,tempo)
    entry = {}
    entry.update(parsed)
    return entry


def add(data,uri):
    ret = make_entry(uri)
    data.append(ret)
    return


def read_input(source):
    ret = []
    with open(source) as infile:
        for line in infile:
            ret.append(parse_url(line))
    return ret


songs = read_input(input_file)

data = []
for uri in songs:
    add(data,uri)

with open(output_file, 'w') as outfile:
    json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii=False)

print("Finished parsing songs from " + input_file)
print("JSON object in: " + output_file)