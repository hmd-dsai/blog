---
title: The incredible comeback of FUTURA to become the GDGoC Vietnam Hackathon 2026 champion
date: 2026-06-21
category: [hackathon, ai, business, reflection]
abstract: "Four freshmen with zero hackathon experience, eliminated in round 2, then pulled back into the final by a disqualification. This is how team FUTURA became national champion, and the lesson we had to learn three times along the way."
---

When they announced the champion of the GDGoC Vietnam Hackathon 2026 and it was us, my whole body went numb and cold. I had never felt anything like it. I was overcome with joy and disbelief at the same moment.

What made it so unreal was that just two weeks earlier, we had been eliminated.

This is the story of how team FUTURA, four freshmen with zero hackathon experience, got from there to the podium, and the lesson we had to learn three times before it finally stuck.

<figure>
  <img src="assets/20260621-1-champion.jpg" alt="Team FUTURA - Champion of GDGoC Hackathon Vietnam 2026" width="700">
  <figcaption>Team FUTURA - Champion of GDGoC Hackathon Vietnam 2026</figcaption>
</figure>

## "Sure, why not?"

Back in March, [@LVĐ](https://www.linkedin.com/in/dong-van-le/) asked me to participate in this competition. I hesitated, since all four of us were first-year students, and none of us had done a hackathon before. But round 1 was only about ideas, with no code required, so I figured, "Why not give it a shot?" I ended up as the team leader.

The theme was *Agentic AI: Agents of Change*. We had two and a half weeks to submit a proposal covering both the tech and the business.

## Round 1: Tearing it all down a week before the deadline

We started well. We agreed on a timeline, split up the work, brainstormed, and settled on an idea we liked: an AI assistant for Hanoi's buses, which don't run on fixed schedules, that would pick your best route from live bus positions.

Then we sent the proposal to a senior for feedback. He told us that our idea (and by extension, every other idea on our list) was an *AI-integrated app*, not an *AI agent system*. He then spent a good while passionately teaching us what agents actually are. Shoutout to [@PĐT](https://www.linkedin.com/in/triducpham/) for this timely intervention :>

That was one week before the deadline, and everything had to go straight into the trash bin.

In the middle of the panic, [@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/) came up with the idea that would carry us to the very end: a multi-agent system for small e-commerce businesses. We met almost every evening, argued over every unclear corner of the proposal, tore into each other's sections, and finished the proposal and slides with two days to spare.

Honestly, I believed round 1 was the only round we were qualified for. We totally had what it takes to write a coherent proposal, but not to build real software. Anyhow, we made it through this round.

## Round 2: Building it the wrong way round

Round 2 involved building an MVP, writing a report, recording a demo, and pitching. We were assigned a mentor and given less than two weeks, even less than round 1.

Our proposal described three agents (Pricing, Content, Customer Service) "working together", with "one agent's output becoming another's input". It sounded great and doable on paper, not gonna lie. In practice, however, we had no idea how they would actually coordinate, or what the product should even look like. To make matters worse, none of us had ever built a web app.

So we just settled for a 50/50 split: two people on the backend (me included), and two on the frontend. We hadn't decided which features we were building.

At this point, you may already guess how that went. It took me days just to get a handful of API endpoints working. Meanwhile, the frontend pair vibe-coded a genuinely good-looking dashboard. When I finally tried to connect the two, I discovered that the features on the frontend and the features on the backend barely overlapped (a Jaccard similarity of 0.5, maybe, if I'm being generous), and that the dashboard was full of demo data hardcoded deep into the components.

The business side got whatever time was left, which turned out to be the last few days (including the time to design the slides). As a result, we mostly recycled the content from round 1's proposal.

On pitch day we gave it everything we had, but we didn't fully understand our own system, let alone the market we were targeting. The Q&A was brutal, and almost all of it was about business:

- "What if the e-commerce platforms never approve your API access?"
- "What if the platforms' own bots are simply better than yours?"
- "When do you break even?"

We couldn't answer all of them adequately. Afterwards, we reached out to an industry expert and asked for a session to rework our business plan. It turned out to be one of the most valuable hours of the whole competition, even if at the time it felt like doing homework for a class we had already failed.

Yeah, because we had. We were eliminated (and devastated), so we decided to move on.

## The universe had mercy on the four crushed souls and decided to give them a second chance

A few days into round 3, during the April 30 to May 1 holiday, we got notified: a team had been disqualified, and as the 7th-placed team (holy moly), we were officially in the final.

My feelings were honestly mixed. I was running on empty after weeks of work, I had already let the competition go, and the holiday was precious time away from university. But of course we were hyped, and we got back to work.

## Round 3: Half the time, half the team

The final meant finishing the product and pitching in person. The top 3 would then face off in a live debate.

Submission was due May 7. The other finalists had been working for about two weeks, while we had just over one. On top of that, two of our four members were in their mandatory military education course and could only help in the evenings. It was [@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/) and me who had to carry most of the work.

This time, we did things in the right order.

[@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/) rebuilt our business case from the ground up, starting not from our agents (what we wanted to build) but from the real pains of e-commerce SMEs: platform fees squeezing already thin margins, customer service teams that can't keep up, more data than anyone has time to read, and content that doesn't convert. Only from those pains did we work out what our solution truly needed, followed by the roadmap, go-to-market plan and finances.

I took the round 2 system apart, removed the features we no longer needed, ripped out the hardcoded demo data, and redefined the product (swapping Pricing for a Risk Manager) as three agents with clear jobs and a clear chain between them:

- **Customer Service** replies to customers in chats and reviews, and picks up insights from negative feedback.
- **Content** creates content plans and posts, either on request or automatically when the Customer Service agent flags something.
- **Risk Manager** wakes up on those same signals, quickly pinpoints product risks, and calls on the other two agents to handle a crisis.

That became Agicom: a multi-agent system that turns what customers are saying into action.

In the evenings, [@NXMĐ](https://www.linkedin.com/in/minh-duc-nguyen-xuan/) and [@LVĐ](https://www.linkedin.com/in/dong-van-le/) reviewed everything we made. [@NXMĐ](https://www.linkedin.com/in/minh-duc-nguyen-xuan/) edited our demo video from the raw footage [@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/) and I recorded, and [@LVĐ](https://www.linkedin.com/in/dong-van-le/) prepared us for rebuttals and helped shape the pitch.

## Demo day

[@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/) and I delivered the pitch, which we framed as a coherent story, and it landed. In the Q&A section, [@LVĐ](https://www.linkedin.com/in/dong-van-le/) carried us for real.

We made the top 3. We hadn't prepared much for the debate, but this time we truly understood our product, and we had studied the other teams' products too. We managed to ask sharp questions, and we held our ground on theirs.

Then the three teams stepped onto the podium, and you know the rest.

## What I'm taking with me

Looking back, every crisis we hit was the same mistake in a different form: starting from the solution instead of the problem.

1. **Customer, then pain point, then solution. Never the other way round.** Round 2's business questions sank us because we had started by brainstorming what our agents could do. Round 3 worked because we started from what SMEs actually struggle with.
2. **Define the system before writing any code, and keep the MVP small.** Our frontend and backend didn't fit together because nobody had decided what we were building. If I don't know what I want, no AI coding tool can figure it out for me.
3. **Understand the fundamentals first.** We almost submitted an "agent" proposal without knowing what an agent was. This competition put me in touch with so much (system design, tech specs, product, business) that I now have a very long reading list.

Finally, to [@LTMN](https://www.linkedin.com/in/minh-ngoc-le-thi-a39874189/), [@LVĐ](https://www.linkedin.com/in/dong-van-le/) and [@NXMĐ](https://www.linkedin.com/in/minh-duc-nguyen-xuan/): thank you for sticking with this through every teardown and every late night. We started out just hoping to learn something, and ended up with far more than we ever aimed for.