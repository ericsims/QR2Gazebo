import pyqrcode, os, shutil, errno, sys


name = '';
if len(sys.argv) > 1 and sys.argv!='':
    name = sys.argv[1]
else:
    print 'No QR code specified!'
    quit();
modeldir = '/root/.gazebo/models/QR_'+name
if os.path.exists(modeldir):
    print name + ' already exists. \nquiting.'
    quit()
#os.makedirs(modeldir)
shutil.copytree('QR_Files/', modeldir)
qr = pyqrcode.create(name)
qr.png(modeldir+'/materials/textures/texture.png', scale=10)
f = open(modeldir+'/model.config', 'r+')
modelconfig = f.read()
modelconfig = modelconfig.replace('[name]','QR_' + name)
f.seek(0)
f.truncate()
f.write(modelconfig)
f.close()
