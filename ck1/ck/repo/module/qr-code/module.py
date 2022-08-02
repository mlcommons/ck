#
# Collective Knowledge (QR code)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: cTuning foundation
#

cfg={}  # Will be updated by CK (meta description of this module)
work={} # Will be updated by CK (temporal data)
ck=None # Will be updated by CK (initialized CK kernel) 

# Local settings
import os

##############################################################################
# Initialize module

def init(i):
    """

    Input:  {}

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0
            }

    """
    return {'return':0}

##############################################################################
# generate QR code

def generate(i):
    """
    Input:  {
              string        - string to convert to qr-code
              (qr_level)    - qr_level (default=3)
              (image_size)  - picture size (default=512)
              (image_type)  - picture type (default=PNG)

              (web)         - if 'yes', return as web output
              (filename)    - file to write (if not web) (default - qr-code.png)
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0


              full_filename - file with image
            }
    """

    o=i.get('con','')

    s=i.get('string','')
    if s=='': return {'return':1, 'error':'string is not defined'}

    qrl=i.get('qr_level','3') # default 3
    ims=i.get('image_size','512')
    imt=i.get('image_type','PNG')

    web=i.get('web','')
    fn=i.get('filename','qr-code.png')

    # Import PyQRNative module
    r=ck.load_module_from_path({'path':work['path'],
                                'module_code_name':'PyQRNative',
                                'cfg':None,
                                'skip_init':'yes'})
    if r['return']>0: return r
    qrm=r['code']

    # Prepare QR code
    qr = qrm.QRCode(int(qrl), qrm.QRErrorCorrectLevel.L)
    qr.addData(s)
    qr.make()
    im = qr.makeImage()
    im1=im.resize((int(ims), int(ims)))

    # Check how to output
    rr={'return':0}

    if web=='yes' or o=='json' or o=='json_out':
       # Generate tmp file
       import tempfile
       fd, fn=tempfile.mkstemp(suffix='.tmp', prefix='ck-')
       os.close(fd)
       os.remove(fn)

    if os.path.isfile(fn):
       return {'return':1, 'error': 'file '+fn+' already exists'}

    # Save image
    try:
       im1.save(fn, imt)
    except Exception as e:
       return {'return':1, 'error':'problem writing image ('+format(e)+')'}

    # Finish web
    if web=='yes' or o=='json' or o=='json_out':
       r=ck.convert_file_to_upload_string({'filename':fn})
       if r['return']>0: return r

       rr['file_content_base64']=r['file_content_base64']
       rr['filename']='qr-code.'+imt.lower()

       os.remove(fn)

    return rr
