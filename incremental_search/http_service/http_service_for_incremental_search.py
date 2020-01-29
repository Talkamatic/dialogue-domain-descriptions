import json

from flask import Flask, request
from jinja2 import Environment

from contacts import CONTACTS, FIRST_NAMES, LAST_NAMES, PHONE_NUMBERS

app = Flask(__name__)
environment = Environment()


def jsonfilter(value):
    return json.dumps(value)


environment.filters["json"] = jsonfilter


def error_response(message):
    response_template = environment.from_string("""
    {
      "status": "error",
      "message": {{message|json}},
      "data": {
        "version": "1.0"
      }
    }
    """)
    payload = response_template.render(message=message)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/selected_contact", methods=['POST'])
def selected_contact():
    try:
        payload = request.get_json()
        first_name_dict = payload["request"]["parameters"]["selected_first_name"]
        last_name_dict = payload["request"]["parameters"]["selected_last_name"]
        first_name = first_name_dict["value"] if first_name_dict else None
        last_name = last_name_dict["value"] if last_name_dict else None
        contacts = available_contacts(first_name, last_name)
        result = []
        for contact_id in contacts:
            full_name = full_name_of(contact_id)
            result.append({"value": contact_id, "sort": "contact", "grammar_entry": full_name})
        return selected_contact_response(result)
    except BaseException as exception:
        return error_response(message=str(exception))


def selected_contact_response(results):
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.0",
        "result": [
        {% for result in results %}
          {
            "value": {{result.value|json}},
            "confidence": 1.0,
            "grammar_entry": {{result.grammar_entry|json}}
          }{{"," if not loop.last}}
        {% endfor %}
        ]
      }
    }
     """)
    payload = response_template.render(results=results)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/call", methods=['POST'])
def call():
    try:
        payload = request.get_json()
        selected_contact = payload["request"]["parameters"]["selected_contact"]["value"]
        number = PHONE_NUMBERS.get(selected_contact)
        return successful_call_response()
    except BaseException as exception:
        return error_response(message=str(exception))


def successful_call_response():
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.0"
      }
    }
    """)
    payload = response_template.render()
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/contact_recognizer", methods=['POST'])
def contact_recognizer():
    try:
        payload = request.get_json()
        utterance = payload["request"]["utterance"]
        language = payload["context"]["language"]
        words = utterance.lower().split()
        results = []
        first_names = _entities_of_first_names(words, language)
        results.extend(first_names)
        last_names = _entities_of_last_names(words, language)
        results.extend(last_names)
        return contact_recognizer_response(results)
    except BaseException as exception:
        return error_response(message=str(exception))


def contact_recognizer_response(entities):
    response_template = environment.from_string("""
    {
      "status": "success",
      "data": {
        "version": "1.0",
        "result": [
        {% for entity in entities %}
          {
            "sort": {{entity.sort|json}},
            "value": {{entity.value|json}},
            "grammar_entry": {{entity.grammar_entry|json}}
          }{{"," if not loop.last}}
        {% endfor %}
        ]
      }
    }
     """)
    payload = response_template.render(entities=entities)
    response = app.response_class(
        response=payload,
        status=200,
        mimetype='application/json'
    )
    return response


def _entities_of_first_names(words, language):
    first_names = FIRST_NAMES[language]
    return _entities_of_names(words, first_names, "first_name")


def _entities_of_last_names(words, language):
    last_names = LAST_NAMES[language]
    return _entities_of_names(words, last_names, "last_name")


def _entities_of_names(words, names, sort):
    result = []
    for name, identifier in list(names.items()):
        if name.lower() in words:
            result.append({"value": identifier, "sort": sort, "grammar_entry": name.lower()})
    return result


def number_of(contact_id):
    number = PHONE_NUMBERS[contact_id]
    return number


def full_name_of(contact_id):
    first_name = first_name_of_contact(contact_id)
    last_name = last_name_of_contact(contact_id)
    full_name = "%s %s" % (first_name, last_name)
    return full_name


def first_name_of_contact(contact):
    identifier = CONTACTS[contact]["first_name"]
    return name_of_identifier(FIRST_NAMES["eng"], identifier)


def last_name_of_contact(contact):
    identifier = CONTACTS[contact]["last_name"]
    return name_of_identifier(LAST_NAMES["eng"], identifier)


def name_of_identifier(names, identifier):
    matching_names = [name for name, actual_id in list(names.items()) if actual_id == identifier]
    assert len(matching_names) == 1, "Expected to find one matching name but found %s for %s among %s" %\
                                         (matching_names, identifier, names)
    return matching_names.pop()


def available_contacts(first_name, last_name):
    matching_first_name_contacts = contacts_with_matching_first_name(first_name)
    matching_last_name_contacts = contacts_with_matching_last_name(last_name)
    available_contacts = matching_first_name_contacts.intersection(matching_last_name_contacts)
    return available_contacts


def first_available_contact(first_name, last_name):
    available_contacts = available_contacts(first_name, last_name)
    assert len(available_contacts) == 1
    selected_contact = available_contacts.pop()
    return selected_contact


def contacts_with_matching_first_name(first_name):
    return contacts_with_matching("first_name", first_name)


def contacts_with_matching_last_name(last_name):
    return contacts_with_matching("last_name", last_name)


def contacts_with_matching(key, value):
    if not value:
        return set(CONTACTS.keys())
    return set([contact_id for contact_id, contact in list(CONTACTS.items()) if contact[key].lower() == value.lower()])
