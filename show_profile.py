import pstats

p = pstats.Stats('profile.status')
p.sort_stats("tottime")

p.print_stats(10)


# profile for -n 10 -p 3 -x stopwords.txt -v verbs.txt pride-and-prejudice.txt

# before optimize
# Tue Oct 30 20:14:19 2018    profile.stats

#          697390 function calls (690360 primitive calls) in 0.650 seconds

#    Ordered by: internal time
#    List reduced from 2079 to 10 due to restriction <10>

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     22391    0.141    0.000    0.141    0.000 C:\Users\v-yizzha\Desktop\WordFrequency\modes.py:102(<listcomp>)
#      1375    0.061    0.000    0.061    0.000 {built-in method nt.stat}
#     22391    0.060    0.000    0.074    0.000 C:\Users\v-yizzha\Desktop\WordFrequency\utils.py:14(get_phrases)
#         1    0.045    0.045    0.382    0.382 C:\Users\v-yizzha\Desktop\WordFrequency\modes.py:83(mode_p)
#     27395    0.039    0.000    0.039    0.000 {method 'split' of 're.Pattern' objects}
#       306    0.023    0.000    0.023    0.000 {built-in method marshal.loads}
#     12/11    0.020    0.002    0.023    0.002 {built-in method _imp.create_dynamic}
#       306    0.017    0.000    0.027    0.000 <frozen importlib._bootstrap_external>:914(get_data)
#     27798    0.011    0.000    0.062    0.000 C:\Users\v-yizzha\AppData\Local\Continuum\anaconda3\envs\nltk\lib\re.py:271(_compile)
# 1067/1064    0.010    0.000    0.039    0.000 {built-in method builtins.__build_class__}

# after optimize
# Tue Oct 30 20:23:31 2018    profile.stats

#          697516 function calls (690485 primitive calls) in 0.510 seconds

#    Ordered by: internal time
#    List reduced from 2094 to 10 due to restriction <10>

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1379    0.060    0.000    0.060    0.000 {built-in method nt.stat}
#     22391    0.058    0.000    0.072    0.000 C:\Users\v-yizzha\Desktop\WordFrequency\utils.py:14(get_phrases)
#         1    0.040    0.040    0.234    0.234 C:\Users\v-yizzha\Desktop\WordFrequency\modes.py:83(mode_p)
#     27395    0.037    0.000    0.037    0.000 {method 'split' of 're.Pattern' objects}
#       304    0.023    0.000    0.023    0.000 {built-in method marshal.loads}
#     12/11    0.018    0.002    0.020    0.002 {built-in method _imp.create_dynamic}
#       308    0.018    0.000    0.028    0.000 <frozen importlib._bootstrap_external>:914(get_data)
#     22391    0.011    0.000    0.011    0.000 C:\Users\v-yizzha\Desktop\WordFrequency\modes.py:102(<listcomp>)
# 1067/1064    0.010    0.000    0.039    0.000 {built-in method builtins.__build_class__}
#     27798    0.010    0.000    0.058    0.000 C:\Users\v-yizzha\AppData\Local\Continuum\anaconda3\envs\nltk\lib\re.py:271(_compile)

# after optimize get_phrases
# Tue Oct 30 20:52:52 2018    profile.status

#          1187822 function calls (1174377 primitive calls) in 0.971 seconds

#    Ordered by: internal time
#    List reduced from 3932 to 10 due to restriction <10>

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      3161    0.110    0.000    0.110    0.000 {built-in method nt.stat}
#     22391    0.096    0.000    0.118    0.000 C:\Users\v-qiyao\Documents\WordFrequency\utils.py:14(get_phrases)
#    100/78    0.059    0.001    0.085    0.001 {built-in method _imp.create_dynamic}
#       742    0.053    0.000    0.053    0.000 {built-in method marshal.loads}
#     27395    0.039    0.000    0.039    0.000 {method 'split' of '_sre.SRE_Pattern' objects}
#         1    0.039    0.039    0.334    0.334 C:\Users\v-qiyao\Documents\WordFrequency\modes.py:83(mode_p)
#    105544    0.037    0.000    0.037    0.000 C:\Users\v-qiyao\AppData\Local\Continuum\anaconda3\lib\site-packages\nltk\probability.py:127(__setitem__)
#       742    0.035    0.000    0.054    0.000 <frozen importlib._bootstrap_external>:830(get_data)
#         1    0.031    0.031    0.068    0.068 {built-in method _collections._count_elements}
#     992/1    0.030    0.000    0.972    0.972 {built-in method builtins.exec}