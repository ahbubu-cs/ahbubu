OVA Pipeline (SIT → UAT → PROD)

1. Service Overview

Automated Jenkins/Groovy pipeline managing code deployments for the Murex trading platform.
Handles build, validation, deployment, and post-deployment checks for the OVA.

2. Stakeholders

Platform operations team and testing team. (monitor build health and release status)

Support teams (for production, and also for some of their own environments)

3. Reliability Goals (SLOs)

| Goal                             | Target     | Measurement Window |
|----------------------------------|:----------:|-------------------:|
| Pipeline success rate            | ≥ 99.5 %   | rolling 30 days    |
| Mean build duration              | ≤ 120 min  | rolling 30 days    |
| Mean recovery time after failure | ≤ 20 min   | per incident       |
| Deployment rollback success      | 100 %      | each incident      |


4. Key SLIs (Metrics)

build_success_rate = successful_builds / total_builds

deployment_duration_seconds (tracked via Jenkins logs)

failed_deployment_recovery_time_minutes

Error count per stage (Jenkins job metrics)

5. Error Budgets & Policy

Error budget = 0.5 % of pipeline failures per month (~2 out of 400 runs).

If exceeded:

Freeze non-urgent changes for one sprint.

Postmortem required for each failure.

Implement automation fix or root-cause prevention before resuming releases.

6. Monitoring & Alerting

Jenkins → Prometheus exporter → Grafana dashboard (builds/hour, success rate).

Slack alerts via Alertmanager when success rate < 99.5 % over 24 hrs.

CloudWatch (if hosted on AWS) to monitor build node health.

7. Toil Reduction & Improvement Actions
Problem	Toil Reduction Plan
Manual rollback	Completed (auto-reversion pipeline)
Manual secrets deployment	Completed (secure secrets pipeline)
Frequent config errors	Add schema validation & linting
Long builds	Implement parallel stages & caching