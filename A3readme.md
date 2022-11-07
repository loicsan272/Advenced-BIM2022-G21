TECHNICAL UNIVERSITY OF DENMARK
MSc Civil Engineering / Architectural Engineering
41934
Advanced Building Information Modeling (BIM)
2022-2023 Autumn Semester
Assignment 3
Lecturer:
Associate Professor Tim Pat McGinley
Students:
Onur Osman Mustafa / s223710
Loic Sansonnens / s221562
Nakaa Aslan / s223111
Date:
06.11.2022
Table of Contents
1. Introduction
2. Use Case Analysis
2.1. Goal
2.2. BIM Use
3. Tool Design
3.1. Process (BPMN)
3.2. Description of Process
4. Information exchange
5. Potential Improvement
5.1. Business Value
5.2. Societal Value
1. Introduction
It is more expensive to repair something poorly done in engineering rather than doing 
it properly in the first place. It is also a case for challenging construction projects since by the 
nature of the industry almost all the productions are unique in their own right, even though 
designs are applied multiple times and they need to comply with the same rules. Promising 
warranty for a predetermined time is also seen in the construction industry. Under the light of 
all these, coming up with certain quality standard is essential for contractors. Quality comes 
with trade offs such as cost, time and constructability. 
Constructability or buildability refer to applicability of the project as a blueprint form 
to the construction site. The production quality of the sites are restrained by the capacity and 
experience of the construction teams. Attention given to the work is also a factor for 
buildability. A work can be realized more coarsely but quickly and cost effectively or more 
meticulously but costly and slowly. Inevitably, meticulous works return better quality hence 
effecting the actual structural strength and integrity of the building. Other side of the medallion 
is the fact that construction is a commercial activity by profit driven establishments which need 
to deliver the projects at desired quality but as fast as possible and as cost effective as possible
which doesn’t go hand in hand with the upmost quality.
Design process in construction contains tons of regulations and norms just like many 
other sectors which can harm people when they don’t produce their products with certain 
seriousness. Variation in the quality of the end product is a very well-known phenomenon in 
construction industry. The sector includes safety coefficients dictated by regulations in various 
forms in the designs, whether increasing the loads or decreasing the strength of the element in 
calculations. The reason for this approach is the quality loss when the blueprint becomes a solid 
three-dimensional building in the site. Overdesign during the calculations is a norm to achieve 
planned strengths in reality because of the losses in the sites.
Construction includes many stages and many parties who are responsible for delivery 
of these stages. All the steps require different specializations; hence they can’t be performed 
by the same team at the same efficiency. Because of that, general contractors must maintain 
working with multiple subcontractors and teams. All site workers bring their own buildability 
and quality trade off. The proposed BIM tool aims to identify a group of bids which satisfies 
quality requirements of the project but still constructable by choosing one bid for every 
production stage.
2. Use Case Analysis
2.1.Goal
Goal of the tool is to determine optimal combination among the bids given by 
construction teams for the tasks during foundation construction in respect to constructability 
and quality which effects strength and structural integrity of the building, inevitably. 
2.2. BIM Use
The tool benefits from size, dimension and placement information of the foundation 
that can be found in the BIM model for its purpose. Depending on the method of choice of the 
general contractor, either the construction teams under the umbrella of general contractor or 
the subcontractors who are tasked with certain steps of the foundation construction can gather 
information about the workload on their shoulders by seeing the size and amount of the 
materials needed for the foundation in the model. They can prepare their own reports to present 
to their superiors. In this case, they are required to inform the project about constructability 
and quality of their bids for the element in question. They can see the structure standing above 
the foundation, they can determine their needs, they can asses their capabilities and provide 
information based on demanded information from them.
3. Tool Design
3.1.Process (BPMN)
3.2. Description of Process
Process is about receiving information about multiple stages of foundation construction 
from the parties who will be responsible of construction works on the field and choosing 
optimal combination regarding their constructability and quality values for the task. BIM 
model is useful for subcontractors since it provides insight about the size of the tasks and the 
proposed tool will determine optimum solution regarding their response.
First of all, the stages of constructing the element in question must be determined in 
order to understand the workforce needed. BIM is a practical tool since it allows seeing 
multiple elements, their size, location and amount at the same time. The later tasks can 
determine the elements that need to be constructed prior. For the case of foundation, the 
construction divided into 9 steps which require different teams with different equipment or 
specialization. 
Retention walls which can be built by multiple different ways if needed; excavation, 
which requires heavy machinery and operators; drainage, which needs pumps and tankers when 
the groundwater is an issue in the site; leveling, which is done by total stations and geotechnics 
teams; preparation of subbase, which is realized by concreting teams and concrete with low 
strength; rebars, which need special equipment for bending, welding and experienced workers; 
formworks, which is done by a different team usually since it requires calculations for the 
weight of the concrete; concreting and curing, which is the responsibility of concreting teams 
or subcontractors and last but not least isolation, which requires different experts are 9 
identified steps for foundation construction.
All steps require different expert teams, all expert teams can provide different quality 
with different constructability levels. After the construction is divided into steps, the 
construction teams can see the work needed via BIM model. Subcontractors or construction 
teams can analyze the model and decide on their own proficiency about the subject. When 
subcontractors come up with a plan to realize their task, they can give an offer to main 
contractor with two different percentages; one for their quality of the work and one for the 
constructability of their work.
Multiple constructions teams or subcontractors propose their bids for the tasks of their 
expertise. The main contractor ends up with multiple bids for multiple assignments. The 
proposed BIM tool helps the main contractors to choose one winning bid for every task 
according to quality and constructability requirements. While the offered quality or 
constructability of winning bid for one task may be below the main contractor’s needs, the code 
would choose other winners in other tasks to reach healthy and optimal average percentages in 
the end when one winner bid for each task is selected.
As a result, a main contractor can reach out to a solution which would provide desired 
quality and constructability with the selected teams in charge, using a tool based on BIM.
4. Information Exchange
The tool enforces information exchange with different parties since the success depends 
on the efficient use of BIM. The information about the dimensions and elements of the 
foundation can be found in the IFC file. If they exist, number of the piles can be learned from 
the IFC file. There are several types of foundations, single footing and continuous footing are 
some of them. Their case requires number and the location of the footings as well and these 
data can be found in the IFC file, if the building was designed in such way. These data, which 
are available in the IFC model, must be taken by subcontractors or construction teams 
responsible for one or multiple tasks in foundation construction.
In the sequential step, the task groups should study the data and provide a bid for the 
tool. The bid should include two parameters in percentages. A percentage for quality and a 
percentage for constructability. Constructability percentage denotes the dedication and ability 
of the bidding task group to the task, it is a result of the complexity of the project, experience, 
speed and willingness to reduce the fineness of the team. They would give themselves a 
constructability rating. Quality percentage is the other side. It mostly depends on the same 
parameters, while they both may benefit from same qualities such as the expertise of the team, 
quality requires the opposite approach in general. This creates the tradeoff between two given 
percentages and creates space for optimization via the proposed BIM tool.
The norms and regulations are also needed to be externally included in the tool because 
the tool has to determine a group of bids by one bid for each task while it pays regard to m 
thresholds. The standards dictated by regulations should be presented as a percentage of quality 
and the ambition of the general contractor must be given as constructability percentage. 
In this case, it is assumed that the subcontractors have deep knowledge of the BIM and 
the tool, they are capable of assessing their abilities accurately and they can complete the task 
as they promised. The tool exists because of the uncertainty of the production quality in the 
sites and if the subcontractors’ values don’t match with reality, the purpose doesn’t materialize.
5. Potential Improvement
5.1.Business Value
The proposed tool for optimizing tradeoff between buildability and quality comes with 
huge benefits in terms of businesses. First of all, sharing information with subcontractors and 
leaving assessment of their own capabilities create time and cost savings for the main 
contractor’s engineering and management teams. It introduces information technologies to the 
parties involved in construction other than engineering and management teams of the general 
contractor, thus increases knowledge and expertise of the area, industry-wide. It increases 
information sharing because of the subcontractors’ access to BIM file.
It increases accuracy of the main contractor’s estimations for delivery and given 
promises by main contractor to the client. It allows main contractor to decide a certain way and 
lean to a certain direction if it is desired since the main contractor can see the capabilities of 
the teams under its management. 
5.2.Societal Value
The buildings are for use of common people. The society would benefit from better and 
more accurate construction practices. As it was mentioned before in the introduction, it is more 
expensive to repair poor products than producing high quality products in the first place. This 
tool would provide more accurate evaluation of the quality of the production since it shrinks 
assessment to smaller levels, thus increases accuracy of assessment. Better evaluation results 
in better chance to achieve desired quality, hence decreases maintenance and repair works 
afterwards, when the building is in use. Repair works are disturbing and messy mostly.
Another value to the society is spared funds. The tool allows contractors to achieve 
desired quality and save more profit for themselves. It creates savings by knowledge not by 
cutting down. Competition in the market may reduce construction costs for the client since the 
construction companies may opt for same profit levels as previous but more competitive price 
to convince the client. This situation returns as fund savings. Savings of public funds may 
return as more investment to social policies or better public services if the client is a state 
agency. If the construction company works with a private partner, then the monetary savings 
can infuse to the economy in a different channel and enhance general circulation.
