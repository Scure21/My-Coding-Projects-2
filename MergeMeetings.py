def merge_ranges(meetings):
    '''
    Given an array containing arrays or tuples with the start and end time of meetings, merge them
    '''

    # sort by start times
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for start, end in sorted_meetings[1:]:

        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the current and last meetings overlap, use the latest end time
        if (start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, end))

        # add the current meeting since it doesn't overlap
        else:
            merged_meetings.append((start, end))

    return merged_meetings