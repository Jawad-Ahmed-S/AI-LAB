from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create the Bayesian Network structure
model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')    
])

cpd_i = TabularCPD(variable='Intelligence',
                   variable_card=2, values=[[0.7], [0.3]], state_names={'Intelligence': ['High', 'Low']})
cpd_s = TabularCPD(variable='StudyHours',
                   variable_card=2, values=[[0.6], [0.4]], state_names={'StudyHours': ['Sufficient', 'Insufficient']})
cpd_d = TabularCPD(variable='Difficulty',
                   variable_card=2, values=[[0.4], [0.6]], state_names={'Difficulty': ['Hard', 'Easy']})


cpd_grade = TabularCPD(
    variable='Grade',
    variable_card=3,
    values=[
        [0.8, 0.9,         0.6, 0.7,         0.4, 0.5,         0.1, 0.2],
        [0.15, 0.08,       0.3, 0.25,        0.4, 0.35,        0.4, 0.5],
        [0.05, 0.02,       0.1, 0.05,        0.2, 0.15,        0.5, 0.3] 
    ],
    evidence=['Intelligence', 'StudyHours', 'Difficulty'],
    evidence_card=[2, 2, 2],
    state_names={'Grade': ['A', 'B', 'C'], 
                 'Intelligence': ['High', 'Low'], 
                 'StudyHours': ['Sufficient', 'Insufficient'],
                 'Difficulty': ['Hard', 'Easy']}
)

cpd_pass = TabularCPD(
    variable='Pass', variable_card=2,
    values=[
        [0.95, 0.80, 0.50], # Yes
        [0.05, 0.20, 0.50]  # No
    ],
    evidence=['Grade'],
    evidence_card=[3],
    state_names={'Pass': ['Yes', 'No'], 'Grade': ['A', 'B', 'C']}
)

model.add_cpds(cpd_i, cpd_s, cpd_d,cpd_grade,cpd_pass)

assert model.check_model()

infer = VariableElimination(model)



result1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'}
)
result2 = infer.query(
    variables=['Intelligent'],
    evidence={'Pass': 'Yes'}
)

print("P(Pass | StudyHours : Sufficient , Difficulty : Hard )")
print(result1)

print("P(Intellligent | Pass : Yes)")
print(result2)
