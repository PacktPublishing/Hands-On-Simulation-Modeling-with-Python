import mdptoolbox.example
P, R = mdptoolbox.example.forest(3,4,2,0.8)

print(P[0])
print(P[1])

print(R[:,0])
print(R[:,1])

gamma=0.9

PolIterModel = mdptoolbox.mdp.PolicyIteration(P, R, gamma)

PolIterModel.run()

print(PolIterModel.V)

print(PolIterModel.policy)

print(PolIterModel.iter)

print(PolIterModel.time)