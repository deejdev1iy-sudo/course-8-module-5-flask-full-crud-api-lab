from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    data = request.get_json()
    if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A title is required"}), 400

    event_id = max((event.id for event in events), default=0) + 1
    new_event = Event(event_id, data["title"].strip())
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    event_update = None
    for event in events:
        if event.id == event_id:
            event_update = event
            break
    if event_update is None:
        return jsonify({"error": "Event not found!"}), 404

    data = request.get_json()
    if not isinstance(data, dict) or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A title is required"}), 400
    
    new_title = data["title"].strip()
    event_update.title = new_title
    return jsonify(event_update.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    event_delete = None
    for event in events:
        if event.id == event_id:
            event_delete = event
            break
    if event_delete is None:
        return jsonify({"error": "Event not  found"}), 404
    
    events.remove(event_delete)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
