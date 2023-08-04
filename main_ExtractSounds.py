import os
import io
import binascii
import struct
import wave
import codecs

from toonpak import extract_pak
from sound import read_index, convert_aud2wav

if __name__ == '__main__':

    #Set the folder where loose PAK and SVL files can be found
    folder = './PAK_DATA/'

    for file in os.listdir(folder):
        if file.endswith(".PAK"):

            filename = os.path.join(folder, file)
            extract_pak(filename)

            with open(filename[:-4] + '/' + file[:-3] + 'SVI', 'rb') as index_file:
                index = read_index(index_file)

            write_raw_ima_adpcm = False

            with open(filename[:-3] + 'SVL', 'rb') as stream_file:
                for idx, (offset, size) in enumerate(index):
                    aud = stream_file.read(size)
                    print(len(aud) - 8)
                    if (write_raw_ima_adpcm):
                        with open(filename[:-4] + '/' + file[:-4] + f'.{idx:04d}.AUD', 'wb') as out_file:
                            out_file.write(aud)

                    with io.BytesIO(aud) as stream:
                        freq, channels, wav = convert_aud2wav(stream)
                    with wave.open(filename[:-4] + '/' + file[:-4] + f'.{idx:04d}.WAV', 'w') as out_file:
                        out_file.setnchannels(channels)
                        out_file.setsampwidth(2) 
                        out_file.setframerate(freq)
                        out_file.writeframesraw(wav)




