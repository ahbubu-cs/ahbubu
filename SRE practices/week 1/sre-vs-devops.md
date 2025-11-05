5 key pillars of devops
1. reduce organization silos
2. accept failures as normal
3. implement gradual change
4. leverage tooling and automation
5. measure everything

SRE implements DevOps. If DevOps is seen as a way of working and SRE is the tools and methods to achieve it.

1. reduce organization silos
share ownership of production with developers

2. accept failure as normal
concept of error budgets. 100% is impossible or very costly to do so. it also means the speed of feature released will be slower. having error budget relieves the stress and can be used strategically for testing.

3. implement gradual change
canary deployments. several types of deployments with pros and cons. canary can be like 95% is on server A and 5% is on server B. There is blue/green, which is switching the entire load 1 to 1. There is rolling deployments, like its name sake, update one node at a time. A/B testing, 50% on each server, decide on which is better.

4. Leverage tooling and automation
Eliminate toil and manual work, programming way and automating this year's job away.

5. measure everything
dashboards and measuring health of systems.