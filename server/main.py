import glob
import shutil
import os
from zipfile import ZipFile

source_path = '../source/*'
destination_path = '../destination'

while True:
    source_obj = glob.glob(source_path)

    for item in range(len(source_obj)):

        if len(source_obj)>0:
            obj_path = source_obj[item]
            obj_name = obj_path.split('/')[-1].split('.')
            server_file = obj_path.split('/')[-1]
            if obj_name[len(obj_name)-1] == 'txt':
                postfix = [1,2,3]
                shutil.copy(obj_path, '.')

                with open(server_file, 'r') as file:
                    lines = file.readlines()
                    file.close()

                prefix = obj_name[0]
                postfix2 = obj_name[1]
                zipObj = ZipFile(f'{prefix}.zip', 'w')

                for item in postfix:
                    file_name =  prefix+'_'+str(item)+'.'+postfix2
                    write_lines = item*10
                    with open(file_name,  'w')  as f:
                        for line in range(write_lines):
                            f.write(lines[line])
                        f.close()

                    zipObj.write(file_name)
                    os.remove(file_name)

                zipObj.close()
                shutil.copy(f'{prefix}.zip',destination_path)
                shutil.unpack_archive(f'{destination_path}/{prefix}.zip', destination_path)
                os.remove(f'{prefix}.zip')
                os.remove(f'{destination_path}/{prefix}.zip')
                os.remove(obj_path)
                os.remove(obj_path.split('/')[-1])
            
            elif obj_name[len(obj_name)-1] == 'py':
                try: 
                    exec(open(f'../source/{server_file}').read())
                except:
                    print('Error occurred in .py file')
                os.remove(obj_path)
