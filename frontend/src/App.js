import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [startTime, setStartTime] = useState('');
    const [endTime, setEndTime] = useState('');
    const [eventType, setEventType] = useState('');
    const [attendees, setAttendees] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const event = {
            title,
            description,
            start_time: startTime,
            end_time: endTime,
            event_type: eventType,
            attendees: attendees.split(',').map(att => att.trim())
        };

        try {
            const response = await axios.post('http://localhost:5000/calendar/add_event', event);
            alert(response.data.message);
        } catch (error) {
            alert(error.response.data.error);
        }
    };

    return (
        <div>
            <h1>Add Event</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Title:
                    <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
                </label>
                <br />
                <label>
                    Description:
                    <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} required />
                </label>
                <br />
                <label>
                    Start Time:
                    <input type="datetime-local" value={startTime} onChange={(e) => setStartTime(e.target.value)} required />
                </label>
                <br />
                <label>
                    End Time:
                    <input type="datetime-local" value={endTime} onChange={(e) => setEndTime(e.target.value)} required />
                </label>
                <br />
                <label>
                    Event Type:
                    <input type="text" value={eventType} onChange={(e) => setEventType(e.target.value)} required />
                </label>
                <br />
                <label>
                    Attendees (comma-separated emails):
                    <input type="text" value={attendees} onChange={(e) => setAttendees(e.target.value)} required />
                </label>
                <br />
                <button type="submit">Add Event</button>
            </form>
        </div>
    );
}

export default App;
