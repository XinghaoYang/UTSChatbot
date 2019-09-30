## story_greet
* greet
 - utter_greet

## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## story_what_can_you_do_02
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_details
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}

## story_details_01
* what_can_you_do
 - utter_what_can_you_do
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}
* details{"code":"c23941"}
 - slot{"code":"c23941"}
 - action_details
 - slot{"code":"23941"}

## story_details_02
* greet
 - utter_greet
* details{"name":"bachelor of science in it"}
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks
* goodbye
 - utter_goodbye

## story_details_03
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* details{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_details
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye

## story_details_04
* greet
 - utter_greet
* details{"code":"31251"}
 - slot{"code":"31251"}
 - action_details
 - slot{"code":"31251"}
* goodbye
 - utter_goodbye

## story_children_01
* greet
    - utter_greet
* details{"code":"41004"}
    - slot{"code":"41004"}
    - action_details
    - slot{"code":"41004"}
* children
    - action_children
    - slot{"code":"41004"}
* children{"code": "c10219"}
    - slot{"code": "c10219"}
    - action_children
    - slot{"code":"10219"}

## story_children_01
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_details
 - slot{"code":"12390"}
* children
 - action_children
 - slot{"code":"12390"}

## story_children_02
* greet
 - utter_greet
* details{"name":"bachelor in business bachelor of science in it"}
 - action_details
 - slot{"code":"10219"}
* children
 - action_children
 - slot{"code":"10219"}
* goodbye
 - utter_goodbye

## story_children_03
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* children{"name":"bachelor of science it"}
 - slot{"code":"10148"}
 - action_children
 - slot{"code":"10148"}
* goodbye
 - utter_goodbye

## story_children_04
* greet
 - utter_greet
* children{"code":"c10219"}
 - slot{"code":"c10219"}
 - action_children
 - slot{"code":"10219"}
* details{"code":"31241"}
 - slot{"code":"31241"}
 - action_details
 - slot{"code":"31241"}
* goodbye
 - utter_goodbye

## story_hons
* greet
 - utter_greet
* honours{"code":"c10148"}
 - slot{"code":"c10148"}
 - action_hons
 - slot{"code":"10148"}
* details
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks

## story_hons_01
* greet
 - utter_greet
* honours{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_hons
 - slot{"code":"23467"}

## story_prof_prac
* greet
 - utter_greet
* prof_prac{"code":"c10148"}
 - slot{"code":"c10148"}
 - action_prof_prac
 - slot{"code":"10148"}
* details
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks

## story_prof_prac_01
* greet
 - utter_greet
* prof_prac{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_prof_prac
 - slot{"code":"23467"}

## story_combined
* greet
 - utter_greet{"code":"c10148"}
* details
 - slot{"code":"c10148"}
 - action_details
 - slot{"code":"10148"}
* combined
 - slot{"code":"c10148"}
 - action_combined
 - slot{"code":"10148"}
* thanks
 - utter_thanks

## story_credit_points
* greet
 - utter_greet
* credit_points{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_credit_points

## story_credit_points_01
* greet
    - utter_greet
* details{"code":"41004"}
    - slot{"code":"41004"}
    - action_details
    - slot{"code":"41004"}
* credit_points
    - action_credit_points
    - slot{"code":"41004"}
* credit_points{"code": "c10219"}
    - slot{"code": "c10219"}
    - action_credit_points
    - slot{"code":"10219"}

## story_credit_points_02
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_credit_points
 - slot{"code":"12390"}
* credit_points
 - action_credit_points
 - slot{"code":"12390"}

## story_credit_points_03
* greet
 - utter_greet
* details{"name":"bachelor in business bachelor of science in it"}
 - action_details
 - slot{"code":"10219"}
* credit_points
 - action_credit_points
 - slot{"code":"10219"}
* goodbye
 - utter_goodbye

## story_credit_points_04
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* credit_points{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_credit_points
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye

## story_credit_points_05
* greet
 - utter_greet
* credit_points{"code":"c10219"}
 - slot{"code":"c10219"}
 - action_credit_points
 - slot{"code":"10219"}
* details
 - slot{"code":"10219"}
 - action_details
* goodbye
 - utter_goodbye

## story_duration
* greet
    - utter_greet
* details{"code":"41004"}
    - slot{"code":"41004"}
    - action_details
    - slot{"code":"41004"}
* duration
    - action_duration
    - slot{"code":"41004"}
* duration{"code": "c10219"}
    - slot{"code": "c10219"}
    - action_duration
    - slot{"code":"10219"}

## story_duration_01
* details{"code":"c12390"}
 - slot{"code":"c12390"}
 - action_credit_points
 - slot{"code":"12390"}
* duration
 - action_duration
 - slot{"code":"12390"}

## story_duration_02
* greet
 - utter_greet
* details{"name":"bachelor in business bachelor of science in it"}
 - action_details
 - slot{"code":"10219"}
* duration
 - action_duration
 - slot{"code":"10219"}
* goodbye
 - utter_goodbye

## story_duration_04
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* duration{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_duration
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye

## story_fees
* greet
 - utter_greet
* fees{"code":"c10148"}
 - slot{"code":"c10148"}
 - action_fees
 - slot{"code":"10148"}
* details
 - action_details
 - slot{"code":"10148"}
* thanks
 - utter_thanks

## story_fees_01
* greet
 - utter_greet
* fees{"code":"c23467"}
 - slot{"code":"c23467"}
 - action_fees
 - slot{"code":"23467"}

## story_atar
* greet
 - utter_greet
* what_can_you_do
 - utter_what_can_you_do
* atar{"code":"c12932"}
 - slot{"code":"c12932"}
 - action_atar
 - slot{"code":"12932"}
* goodbye
 - utter_goodbye

## story_atar_01
* greet
 - utter_greet
* details{"code":"c10219"}
 - slot{"code":"c10219"}
 - action_details
 - slot{"code":"10219"}
* atar
 - slot{"code":"10219"}
 - action_atar
* goodbye
 - utter_goodbye

## story_years
* greet
 - utter_greet
* years{"code":"12932"}
 - slot{"code":"12932"}
 - action_years

 ## story_years_entities
* greet
 - utter_greet
* years_entities{"code":"12932","name":"Bachelor of Information Technology"}
 - slot{"code":"12932","name":"Bachelor of Information Technology"}
 - action_years_entities
