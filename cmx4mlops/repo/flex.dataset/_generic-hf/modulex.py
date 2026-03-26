# Author and developer: Grigori Fursin



def install(i):

    cmind = i['cmind']
    self_meta = i['self_meta']

    return cmind.x({'automation': self_meta['use']['flex.common'],
                    'action':'download_hf',
                    'input': i,
                    'key': 'dataset'})
