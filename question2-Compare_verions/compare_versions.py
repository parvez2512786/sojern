def compare_versions(version1,version2):
  ver1=[int(i) for i in version1.split(".")]
  ver2=[int(i) for i in version2.split(".")]
  for j in range(max((len(ver1),len(ver2)))):
    if j < len(ver1):
      v1=ver1[j]
    else:
      v1=0
    if j < len(ver2):
      v2=ver2[j]
    else:
      v2=0
    if v1 > v2:
      return 1
    elif v2 > v1:
      return -1
  else:
    return 0

print(compare_versions("1.2.9.9.9","1.3"))