import pandas as pd
import gurobipy as gp
from gurobipy import quicksum
from gurobipy import GRB

df = pd.read_excel('data.xlsx')
r = df['release date d_j'].values.tolist()
p = df['processing length p_j'].values.tolist()


# 建新模型
model = gp.Model("SB")

# 參數
n = 12 
M = 10000  

# 建立變數

C = {}

for j in range(n):
    C[j] = model.addVar(vtype=GRB.INTEGER, name=f"C_{j}")
    
x = model.addVars(n,n,vtype=GRB.BINARY)

#更新
model.update()

# 目標函數
model.setObjective(quicksum(C[j] for j in range(n)), GRB.MINIMIZE)

# 限制式
for i in range(n):
    for j in range(n):
        if i != j:
            model.addConstr(x[i, j] + x[j, i] == 1, name="Constr1_{i}_{j}")
            model.addConstr(C[j] - p[j] + (1 - x[i, j]) * M >= C[i], name="Constr3_{i}_{j}")


model.addConstrs(C[j] - (r[j] + p[j]) >= 0 for j in range(n))
model.addConstrs(C[j] >= 0 for j in range(n))

model.optimize()

# model2
'''m2 = gp.Model("PB")

x = m2.addVars(n,n,vtype=GRB.BINARY)
for k in range(n):
    C[k] = model.addVar(lb = 0,vtype=GRB.INTEGER)

model.setObjective(quicksum(C[k] for k in range(n)), GRB.MINIMIZE)

model.addConstrs(quicksum(x[j, k] for k in range(n) for j in range(n)) == 1)
model.addConstrs(quicksum(x[j, k] for j in range(n) for k in range(n)) == 1)
model.addConstr(C[1]-quicksum(x[j,1]*(r[j]+p[j]) for j in range(n)) >= 0)
model.addConstrs(C[k]-C[k-1]-quicksum(x[j,k]*p[j] for j in range(n)) >= 0 for k in range(1,n))
model.addConstrs(C[k]-quicksum(x[j,k]*r[j] for j in range(n)) >= 0 for k in range(1,n))  '''

# model3
m3 = gp.Model("TI")
x = m3.addVars(n,n,vtype=GRB.BINARY)
for j in range(n):
    C[j] = model.addVar(lb = 0,vtype=GRB.INTEGER)

model.setObjective(quicksum(C[j] for j in range(n)), GRB.MINIMIZE)

model.addConstr()

# print結果
if model.status == GRB.OPTIMAL:
    print("Optimal solution found")
    for i in range(n):
        print(f"C_{i} = {C[i].X}")
    
else:
    print("No solution found")
