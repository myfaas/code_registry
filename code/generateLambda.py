import random
import json
from collections import OrderedDict

packageFilePath = "packages"

# 加载依赖包
with open(packageFilePath) as f:
    data = f.readlines()
    packages = [d[:-1] for d in data]
    print(packages)


# 生成python文件
def genPYFile(packs, filename):
    # packs: 依赖列表
    with open(filename, 'w') as f:
        packs = ['import ' + p + '\n' for p in packs]
        packs.append('\ndef main():\n')
        packs.append('  return \'' + filename + ' done!\'\n')
        f.writelines(packs)


# 生成50个函数
prob = [0.3, 0.4, 0.5, 0.6, 0.7]
i = 1
lambda_info = OrderedDict()
for pro in prob:
    for _ in range(10):
        target = []
        for pac in packages:
            x = random.random()
            if x > pro:
                target.append(pac)
        # 生成一个文件
        genPYFile(target, './lambdas/lambda_' + str(i) + '.py')
        lambda_info['lambda_' + str(i)] = target
        i += 1

json_str = json.dumps(lambda_info, indent=4)
with open('lambdas.json', 'w') as json_file:
    json_file.write(json_str)
