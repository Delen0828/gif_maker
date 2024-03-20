process_json() {
    root_dir="$1"
    jq -c '.[]' "$root_dir/Plot.json" | while IFS= read -r item; do
        name=$(jq -r '.name' <<< "$item")
        video=$(jq -r '.video' <<< "$item")
        # echo "Name: $name, Video: $video"
        cp "$root_dir/$video" "out/$name"
    done
}

# Example usage:
process_json "seq_notrace_his2.0/videos/480p30/sections" &
process_json "seq_notrace_his3.0/videos/480p30/sections" &
process_json "seq_notrace_his4.0/videos/480p30/sections" &
process_json "seq_notrace_his5.0/videos/480p30/sections" &
process_json "seq_notrace_his6.0/videos/480p30/sections" &
process_json "seq_notrace_his7.0/videos/480p30/sections" &
process_json "seq_notrace_his8.0/videos/480p30/sections" &
# process_json "seq_notrace_his9.0/videos/480p30/sections" &
# process_json "seq_notrace_his10.0/videos/480p30/sections" &

process_json "seq_trace_nohis2.0/videos/480p30/sections" &
process_json "seq_trace_nohis3.0/videos/480p30/sections" &
process_json "seq_trace_nohis4.0/videos/480p30/sections" &
process_json "seq_trace_nohis5.0/videos/480p30/sections" &
process_json "seq_trace_nohis6.0/videos/480p30/sections" &
process_json "seq_trace_nohis7.0/videos/480p30/sections" &
process_json "seq_trace_nohis8.0/videos/480p30/sections" &
# process_json "seq_trace_nohis9.0/videos/480p30/sections" &
# process_json "seq_trace_nohis10.0/videos/480p30/sections" & 


process_json "seq_trace_his2.0/videos/480p30/sections" &
process_json "seq_trace_his3.0/videos/480p30/sections" &
process_json "seq_trace_his4.0/videos/480p30/sections" &
process_json "seq_trace_his5.0/videos/480p30/sections" &
process_json "seq_trace_his6.0/videos/480p30/sections" &
process_json "seq_trace_his7.0/videos/480p30/sections" &
process_json "seq_trace_his8.0/videos/480p30/sections" &
# process_json "seq_trace_his9.0/videos/480p30/sections" &
# process_json "seq_trace_his10.0/videos/480p30/sections" &  


process_json "seq_notrace_nohis2.0/videos/480p30/sections" &
process_json "seq_notrace_nohis3.0/videos/480p30/sections" &
process_json "seq_notrace_nohis4.0/videos/480p30/sections" &
process_json "seq_notrace_nohis5.0/videos/480p30/sections" &
process_json "seq_notrace_nohis6.0/videos/480p30/sections" &
process_json "seq_notrace_nohis7.0/videos/480p30/sections" &
process_json "seq_notrace_nohis8.0/videos/480p30/sections" &
# process_json "seq_notrace_nohis9.0/videos/480p30/sections" &
# process_json "seq_notrace_nohis10.0/videos/480p30/sections" &

process_json "sync_trace2.0/videos/480p30/sections" &
process_json "sync_trace3.0/videos/480p30/sections" &
process_json "sync_trace4.0/videos/480p30/sections" &
process_json "sync_trace5.0/videos/480p30/sections" &
process_json "sync_trace6.0/videos/480p30/sections" &
process_json "sync_trace7.0/videos/480p30/sections" &
process_json "sync_trace8.0/videos/480p30/sections" &
# process_json "sync_trace9.0/videos/480p30/sections" &
# process_json "sync_trace10.0/videos/480p30/sections" &
 
process_json "sync_notrace2.0/videos/480p30/sections" &
process_json "sync_notrace3.0/videos/480p30/sections" &
process_json "sync_notrace4.0/videos/480p30/sections" &
process_json "sync_notrace5.0/videos/480p30/sections" &
process_json "sync_notrace6.0/videos/480p30/sections" &
process_json "sync_notrace7.0/videos/480p30/sections" &
process_json "sync_notrace8.0/videos/480p30/sections" &
# process_json "sync_notrace9.0/videos/480p30/sections" &
# process_json "sync_notrace10.0/videos/480p30/sections"

process_json "static2.0/videos/480p30/sections" &
process_json "static3.0/videos/480p30/sections" &
process_json "static4.0/videos/480p30/sections" &
process_json "static5.0/videos/480p30/sections" &
process_json "static6.0/videos/480p30/sections" &
process_json "static7.0/videos/480p30/sections" &
process_json "static8.0/videos/480p30/sections"