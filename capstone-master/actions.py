# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import directory_loader as dl

d = dl.Directory()
map = {
    "":"when does 48024 in  take classes?",
            "bachelor of information technology":"Bachelor of Information Technology",
            "bachelor of science ( honours ) in information technology":"Bachelor of Science (Honours) in Information Technology",
            "business information systems management in bachelor of science in information technology":"Business Information Systems Management in Bachelor of Science in Information Technology",
            "data analytics in bachelor of science in information technology":"Data Analytics in Bachelor of Science in Information Technology",
            "enterprise systems development in bachelor of science in information technology":"Enterprise Systems Development in Bachelor of Science in Information Technology",
            "interaction design in bachelor of science in information technology":"Interaction Design in Bachelor of Science in Information Technology",
            "networking and cybersecurity in bachelor of science in information technology":"Networking and Cybersecurity in Bachelor of Science in Information Technology",
            "business information systems management in bachelor of computing science":"Business Information Systems Management in Bachelor of Computing Science (Honours)",
            "interaction design in bachelor of computing science":"Interaction Design in Bachelor of Computing Science (Honours)",
            "networking and cybersecurity in bachelor of computing science":"Networking and Cybersecurity in Bachelor of Computing Science (Honours)",
            "enterprise systems development in bachelor of computing science":"Enterprise Systems Development in Bachelor of Computing Science (Honours)",
            "artificial intelligence and data analytics in bachelor of computing science":"Artificial Intelligence and Data Analytics in Bachelor of Computing Science (Honours)",
            "mathematical analysis in bachelor of computing science":"Mathematical Analysis in Bachelor of Computing Science (Honours)",
            "operations research in bachelor of computing science":"Operations Research in Bachelor of Computing Science (Honours)",
            "statistics in bachelor of computing science":"Statistics in Bachelor of Computing Science (Honours)",
            "cybersecurity and privacy in bachelor of computing science":"Cybersecurity and Privacy in Bachelor of Computing Science (Honours)",
        }

def init_code(dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("run init_code")

        try:
            input_type = tracker.latest_message['entities'][0]['entity']
            value = tracker.latest_message['entities'][0]['value']
            print("run try")
            print(input_type)
            print(value)
        except:
            print("run except")
            input_type = 'code'
            value = tracker.get_slot('code')

        if not value:
            dispatcher.utter_template('utter_fallback', tracker)
            return None

        if input_type == 'name':
            results = d.search(value)
            if len(results) == 0:
                dispatcher.utter_template("utter_code_does_not_exist", tracker, name=value)
                return None
            elif len(results) > 1:
                dispatcher.utter_message('There are multiple results for {}:'.format(value))
                for r in results:
                    i = d[r[0]]
                    dispatcher.utter_message('{} {}'.format(i.code(), i.get_name()))
                dispatcher.utter_message('Please reply with the correct code.')
                return None
            else:
                result = d[results[0][0]]

        elif input_type == 'code':
            try:
                result = d[value]
            except KeyError:
                dispatcher.utter_template("utter_code_does_not_exist", tracker, code=value)
                return None
        else:
            dispatcher.utter_template('utter_fallback', tracker)
            return None

        return result


class ActionDetails(Action):
    def name(self) -> Text:
        return "action_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        print("run ActionDetails")

        dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                        result.get_name(),
                                                                                        result.get_type(),
                                                                                        result.url()))
        return [SlotSet("code", result.just_code())]

class ActionChildren(Action):
    def name(self) -> Text:
        return "action_children"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        if not result.is_type(''):
            dispatcher.utter_message('{} {} is a {} at UTS. It contains:'.format(result.code(),
                                                                                 result.get_name(),
                                                                                 result.get_type()))
            for c in result.get_children():
                dispatcher.utter_message('{} {}'.format(c.code(), c.get_name()))
            else:
                dispatcher.utter_message('For more info, visit {}'.format(result.url()))
        else:
            dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                            result.get_name(),
                                                                                            result.get_type(),
                                                                                            result.url()))
        return [SlotSet("code", result.just_code())]

class ActionChildren(Action):
    def name(self) -> Text:
        return "action_children"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        if result is None:
            return []

        print("run ActionChildren")

        if not result.is_type(''):
            dispatcher.utter_message('{} {} is a {} at UTS. It contains:'.format(result.code(),
                                                                                 result.get_name(),
                                                                                 result.get_type()))
            for c in result.get_children():
                if c.is_type('xbk'):
                    s = 'Select {} credit points from '.format(c.cp())
                    c_children = c.get_children()
                    if len(c_children) > 1:
                        for c_ in c_children[0:-1]:
                            s += c_.code() + ' ' + c_.get_name() + ', '
                        s += 'and '
                    if c_children[-1] is not None:
                        s += c_children[-1] .code() + ' ' + c_children[-1].get_name()
                    s += '.'
                    dispatcher.utter_message(s)
                else:
                    dispatcher.utter_message('{} {}'.format(c.code(), c.get_name()))
            else:
                dispatcher.utter_message('For more info, visit {}'.format(result.url()))
        else:
            dispatcher.utter_message('{} {} is a {} at UTS. For more info, visit {}'.format(result.code(),
                                                                                            result.get_name(),
                                                                                            result.get_type(),
                                                                                            result.url()))
        return [SlotSet("code", result.just_code())]


class ActionHonours(Action):
    def name(self) -> Text:
        return "action_hons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionHonours")

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_hons():
                dispatcher.utter_message('{} {} is a honours degree.'.format(result.code(), result.get_name()))
            else:
                dispatcher.utter_message('{} {} is not a honours degree.'.format(result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]


class ActionProfPrac(Action):
    def name(self) -> Text:
        return "action_prof_prac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionProfPrac")

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_prof_prac():
                dispatcher.utter_message('{} {} comes with a Diploma in Professional Practice.'.format(result.code(),
                                                                                                       result.get_name()))
            else:
                dispatcher.utter_message('{} {} does not come with a Diploma in Professional Practice.'.format(
                    result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]


class ActionCombined(Action):
    def name(self) -> Text:
        return "action_combined"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionCombined")

        if result is None:
            return []

        elif result.is_type('c'):
            if result.is_combined():
                dispatcher.utter_message(
                    '{} {} is a combined degree.'.format(result.code(), result.get_name()))
            else:
                dispatcher.utter_message(
                    '{} {} is not a combined degree.'.format(result.code(), result.get_name()))

        else:
            dispatcher.utter_message('{} {} is not a course at UTS. It is a a {} at UTS. It contains:'.format(
                result.code(), result.get_name(), result.get_type()))
        return [SlotSet("code", result.just_code())]


class ActionCreditPoints(Action):
    def name(self) -> Text:
        return "action_credit_points"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionCreditPoints")

        if result is None:
            return []

        elif not result.is_type(''):
            dispatcher.utter_message(
                '{} {} is a {} with {} credit points.'.format(result.code(), result.get_name(), result.get_type(),
                                                              result.cp()))

        else:
            dispatcher.utter_message('{} {} consists of {} credit points in total.'.format(result.code(),
                                                                                           result.get_name(),
                                                                                           result.cp()))
        return [SlotSet("code", result.just_code())]


class ActionDuration(Action):
    def name(self) -> Text:
        return "action_duration"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        full_load = 48

        print("run ActionDuration")

        if result is None:
            return []

        elif result.is_type('c'):
            years = round(result.cp()/full_load)
            dispatcher.utter_message(
                '{} {} has {} credit points which can be completed for {} years full time.'.format(result.code(),
                                                                                                   result.get_name(),
                                                                                                   result.cp(),
                                                                                                   years))

        else:
            dispatcher.utter_message('{} {} is not a course.'.format(result.code(), result.get_name()))
        return [SlotSet("code", result.just_code())]


class ActionFees(Action):
    def name(self) -> Text:
        return "action_fees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionFees")

        url = 'https://cis.uts.edu.au/fees/course-fees.cfm'

        dispatcher.utter_message('For fee details please visit {}.'.format(url))

        return [SlotSet("code", result.just_code())]


class ActionAtar(Action):
    def name(self) -> Text:
        return "action_atar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        result = init_code(dispatcher, tracker, domain)

        print("run ActionAtar")

        if result is None:
            return []

        elif result.is_type('c'):
            atar = result.get_atar()
            if atar is None:
                dispatcher.utter_message('Admission for {} {} is not based on ATAR. For more info, visit {}'.format(
                    result.code(), result.get_name(), result.url()))
            else:
                dispatcher.utter_message('{} {} has a ATAR requirement of {}.'.format(result.code(),
                                                                                      result.get_name(),
                                                                                      atar))

        else:
            dispatcher.utter_message('{} {} is not a course.'.format(result.code(), result.get_name()))
        return [SlotSet("code", result.just_code())]


class ActionYear(Action):
    def name(self) -> Text:
        return "action_years"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        result = init_code(dispatcher, tracker, domain)

        print("run ActionYear")

        years = result.get_years()

        for key in years:
            if years[key] is not '':
                if int(years[key]) > 0:
                    dispatcher.utter_message(
                        '[{}]{} of {} is in the {} semester'.format(result.code(), result.get_name(), key, years[key]))
                else:
                    dispatcher.utter_message(
                        '[{}]{} of {} is an elective course'.format(result.code(), result.get_name(), key))
            else:
                dispatcher.utter_message(
                    '[{}]{} is not a course of {}'.format(result.code(), result.get_name(), key))

class ActionYearEntities(Action):
    def name(self) -> Text:
        return "action_years_entities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        result = init_code(dispatcher, tracker, domain)


        name = tracker.latest_message['entities'][1]['entity']
        value = tracker.latest_message['entities'][1]['value']
        class_name = map[value]
        print(value)
        print(class_name)

        print("run ActionYearEntites")

        years = result.get_years()

        semester = years[class_name]

        if semester is not '':
            if int(semester) > 0:
                dispatcher.utter_message(
                    '[{}]{} of {} is in the {} semester'.format(result.code(), result.get_name(), class_name, semester))
            else:
                dispatcher.utter_message(
                    '[{}]{} of {} is an elective course'.format(result.code(), result.get_name(), class_name))
        else:
            dispatcher.utter_message(
                '[{}]{} is not a course of {}'.format(result.code(), result.get_name(), class_name))

