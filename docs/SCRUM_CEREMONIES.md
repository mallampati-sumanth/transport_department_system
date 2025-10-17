# Scrum Ceremonies Guide - Transport Department System

## Overview

Scrum ceremonies (also called events or meetings) are time-boxed activities that create regularity and minimize the need for undefined meetings. This guide outlines how to conduct each ceremony for the Transport Department System project.

---

## 1. Sprint Planning

**Purpose**: Plan the work to be performed in the Sprint

**Attendees**: 
- Product Owner (Required)
- Scrum Master (Required)
- Development Team (Required)

**Duration**: 2 hours for a 2-week sprint (4 hours maximum)

**When**: First day of the sprint

### Agenda

#### Part 1: What can be done? (1 hour)
1. **Review Sprint Goal**
   - Product Owner presents the sprint objective
   - Team discusses and agrees on the goal

2. **Select Product Backlog Items**
   - Product Owner presents prioritized items
   - Team asks clarifying questions
   - Team forecasts what can be completed

3. **Check Team Capacity**
   - Account for holidays, vacations, meetings
   - Consider technical debt and dependencies

#### Part 2: How will it get done? (1 hour)
1. **Break Down User Stories**
   - Decompose selected stories into tasks
   - Identify technical approach
   - Estimate task hours (optional)

2. **Create Sprint Backlog**
   - List all tasks needed to complete stories
   - Assign initial ownership (can change during sprint)
   - Identify dependencies and risks

3. **Finalize Sprint Commitment**
   - Team commits to delivering the increment
   - Sprint Goal is confirmed

### Outputs
- Sprint Goal
- Sprint Backlog
- Definition of Done (reviewed/updated)

### Example Sprint Goal
"Establish core vehicle and driver management functionality with database persistence and API endpoints"

---

## 2. Daily Standup (Daily Scrum)

**Purpose**: Synchronize activities and create a plan for the next 24 hours

**Attendees**: 
- Development Team (Required)
- Scrum Master (Required)
- Product Owner (Optional)

**Duration**: 15 minutes (strictly time-boxed)

**When**: Every day at the same time (9:00 AM recommended)

### Format

Each team member answers three questions:
1. **What did I complete yesterday?**
   - Focus on done items that move sprint forward
   
2. **What will I work on today?**
   - Commit to specific tasks
   
3. **Are there any impediments?**
   - Blockers preventing progress
   - Issues needing Scrum Master attention

### Best Practices

- **Stand up** - Keeps meeting short
- **Same time, same place** - Creates routine
- **Stay focused** - No detailed discussions
- **Update board** - Reflect progress visually
- **Parking lot** - Note items for follow-up

### Example Standup

**Developer 1:**
- Yesterday: Completed Vehicle model with unit tests
- Today: Will implement Driver model
- Blockers: None

**Developer 2:**
- Yesterday: Set up database schema, fixed migration issues
- Today: Will work on API endpoints for vehicles
- Blockers: Waiting for code review on PR #12

**Developer 3:**
- Yesterday: Researched route optimization algorithms
- Today: Will implement Route model
- Blockers: Need clarification on route assignment logic (will discuss after standup)

### Anti-Patterns to Avoid

❌ Turning into status report to Scrum Master
❌ Problem-solving during standup
❌ Late starts or going over time
❌ Team members not listening to each other
❌ Skipping standup because "nothing changed"

---

## 3. Sprint Review

**Purpose**: Inspect the increment and adapt the Product Backlog

**Attendees**: 
- Scrum Team (Required)
- Stakeholders (Required)
- Key users (Optional)

**Duration**: 1 hour for 2-week sprint (2 hours maximum)

**When**: Last day of the sprint

### Agenda

1. **Welcome and Context** (5 minutes)
   - Scrum Master welcomes attendees
   - Review sprint goal
   - Overview of what was planned vs. completed

2. **Demo Completed Work** (40 minutes)
   - Development Team demonstrates features
   - Only show "Done" items (meet Definition of Done)
   - Live demonstration preferred over slides
   - Encourage questions and interaction

3. **Discuss What Didn't Get Done** (5 minutes)
   - Explain why items weren't completed
   - Review impediments encountered
   - No blame, focus on learning

4. **Stakeholder Feedback** (10 minutes)
   - Gather feedback on demonstrated features
   - Discuss changes in market or requirements
   - Identify new opportunities

5. **Review Product Backlog** (10 minutes)
   - Update backlog based on feedback
   - Adjust priorities if needed
   - Discuss likely next sprint items

### Outputs
- Feedback on completed work
- Updated Product Backlog
- Potential changes for next sprint

### Demo Checklist

- [ ] Environment is set up and tested
- [ ] Sample data is loaded
- [ ] Demo script is prepared
- [ ] Backup plan ready (screenshots, video)
- [ ] Stakeholders are invited and confirmed
- [ ] Room/virtual meeting is ready

### Example Demo Flow

1. **Introduction**: "In this sprint, we focused on vehicle management"
2. **Feature 1**: "Let me show you how to add a new vehicle..."
3. **Feature 2**: "Now I'll demonstrate the vehicle listing API..."
4. **Feature 3**: "Here's how we track vehicle status..."
5. **Q&A**: Address questions and gather feedback

---

## 4. Sprint Retrospective

**Purpose**: Reflect on the sprint and plan improvements

**Attendees**: 
- Development Team (Required)
- Scrum Master (Required)
- Product Owner (Optional)

**Duration**: 1 hour for 2-week sprint (1.5 hours maximum)

**When**: After Sprint Review, before next Sprint Planning

### Agenda

1. **Set the Stage** (5 minutes)
   - Create safe environment
   - Review retrospective goal
   - Agree on format

2. **Gather Data** (15 minutes)
   - Collect facts about sprint
   - Review metrics (velocity, burndown)
   - Share observations

3. **Generate Insights** (20 minutes)
   - Discuss what went well
   - Identify what could improve
   - Recognize achievements

4. **Decide Actions** (15 minutes)
   - Brainstorm improvements
   - Prioritize actions
   - Commit to 2-3 actionable items

5. **Close** (5 minutes)
   - Summarize action items
   - Assign owners
   - Thank participants

### Common Formats

#### Start-Stop-Continue
- **Start**: What should we start doing?
- **Stop**: What should we stop doing?
- **Continue**: What should we keep doing?

#### Glad-Sad-Mad
- **Glad**: What made us happy?
- **Sad**: What disappointed us?
- **Mad**: What frustrated us?

#### 4 L's
- **Liked**: What did we enjoy?
- **Learned**: What did we discover?
- **Lacked**: What was missing?
- **Longed For**: What do we wish for?

### Outputs
- Action items for improvement
- Assigned owners
- Timeline for implementation
- Updated working agreements (if needed)

### Example Action Items

1. **Improve code review turnaround**
   - Owner: Team
   - Action: Commit to reviewing PRs within 24 hours
   - Timeline: Starting next sprint

2. **Better estimation accuracy**
   - Owner: Scrum Master
   - Action: Add estimation poker session to planning
   - Timeline: Next sprint planning

3. **Reduce technical debt**
   - Owner: Tech Lead
   - Action: Allocate 20% of sprint capacity to refactoring
   - Timeline: Next sprint onwards

---

## 5. Backlog Refinement (Grooming)

**Purpose**: Prepare backlog items for future sprints

**Attendees**: 
- Product Owner (Required)
- Development Team (Required)
- Scrum Master (Facilitator)

**Duration**: 1-2 hours per week (ongoing)

**When**: Mid-sprint, as needed

### Activities

1. **Review Upcoming Items**
   - Examine top priority backlog items
   - Ensure clarity and detail

2. **Add Details**
   - Write/refine acceptance criteria
   - Add technical notes
   - Attach mockups or diagrams

3. **Estimate Stories**
   - Use planning poker or other technique
   - Assign story points
   - Identify large items to split

4. **Split Large Items**
   - Break down epics into user stories
   - Ensure stories fit in one sprint
   - Maintain vertical slices

5. **Order Backlog**
   - Confirm priority
   - Consider dependencies
   - Balance value and risk

### Definition of Ready

Before a story enters a sprint, it should be:
- [ ] Clearly described
- [ ] Have acceptance criteria
- [ ] Estimated by team
- [ ] Small enough for one sprint
- [ ] Dependencies identified
- [ ] Testable

---

## Ceremony Calendar (2-Week Sprint Example)

### Week 1
**Monday**
- 9:00 AM: Sprint Planning (2 hours)
- After Planning: Start development

**Tuesday - Friday**
- 9:00 AM: Daily Standup (15 minutes)

**Wednesday (mid-sprint)**
- 2:00 PM: Backlog Refinement (1 hour)

### Week 2
**Monday - Thursday**
- 9:00 AM: Daily Standup (15 minutes)

**Friday (last day)**
- 9:00 AM: Daily Standup (15 minutes)
- 2:00 PM: Sprint Review (1 hour)
- 3:30 PM: Sprint Retrospective (1 hour)
- Prepare for next Sprint Planning

---

## Tips for Effective Ceremonies

### General Best Practices

1. **Time-box everything** - Respect people's time
2. **Come prepared** - Review materials beforehand
3. **Stay focused** - Defer tangents to parking lot
4. **Be present** - Minimize distractions
5. **Action-oriented** - Every meeting should produce outcomes

### Remote Ceremonies

- Use video conferencing tools (Zoom, Teams)
- Share screens for demos and collaboration
- Use virtual whiteboards (Miro, Mural)
- Record sessions for absent members
- Send calendar invites with agendas

### Facilitation Tips

- **Start on time** - Even if not everyone is present
- **End on time** - Or early if objectives are met
- **Keep energy high** - Use icebreakers, vary activities
- **Encourage participation** - Draw out quiet voices
- **Capture output** - Document decisions and actions

---

## Common Pitfalls

### Sprint Planning
❌ Not having refined backlog
❌ Over-committing the team
❌ Skipping the "how" discussion
❌ Product Owner not present

### Daily Standup
❌ Turning into problem-solving session
❌ Going over 15 minutes
❌ Status report to manager
❌ Not identifying impediments

### Sprint Review
❌ Showing incomplete work
❌ Making it a slideshow
❌ Not inviting stakeholders
❌ Skipping feedback discussion

### Sprint Retrospective
❌ Pointing fingers/blaming
❌ Not creating action items
❌ Same discussions every time
❌ Product Owner dominating

---

## Continuous Improvement

Ceremonies themselves should be inspected and adapted:

- **Retrospect the retrospectives** - Every few sprints
- **Experiment with formats** - Try new techniques
- **Measure effectiveness** - Survey participants
- **Adapt to team needs** - What works for your context?

Remember: Scrum ceremonies are designed to enable transparency, inspection, and adaptation. They should add value, not be bureaucratic overhead.

---

## Resources

- [Scrum Guide](https://scrumguides.org/) - Official Scrum framework
- [Sprint Planning](https://www.scrum.org/resources/what-is-sprint-planning) 
- [Daily Scrum](https://www.scrum.org/resources/what-is-a-daily-scrum)
- [Sprint Review](https://www.scrum.org/resources/what-is-a-sprint-review)
- [Sprint Retrospective](https://www.scrum.org/resources/what-is-a-sprint-retrospective)
