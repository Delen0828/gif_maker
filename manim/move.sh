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
process_json "static2/videos/480p60/sections" &
process_json "static3/videos/480p60/sections" &
process_json "static4/videos/480p60/sections" &

process_json "seq_notrace_his2/videos/480p60/sections" &
process_json "seq_notrace_his3/videos/480p60/sections" &
process_json "seq_notrace_his4/videos/480p60/sections" &
 
process_json "seq_trace_nohis2/videos/480p60/sections" &
process_json "seq_trace_nohis3/videos/480p60/sections" &
process_json "seq_trace_nohis4/videos/480p60/sections" &
 
process_json "seq_trace_his2/videos/480p60/sections" &
process_json "seq_trace_his3/videos/480p60/sections" &
process_json "seq_trace_his4/videos/480p60/sections" &
 
process_json "seq_notrace_nohis2/videos/480p60/sections" &
process_json "seq_notrace_nohis3/videos/480p60/sections" &
process_json "seq_notrace_nohis4/videos/480p60/sections" &
 
process_json "sync_trace2/videos/480p60/sections" &
process_json "sync_trace3/videos/480p60/sections" &
process_json "sync_trace4/videos/480p60/sections" &
 
process_json "sync_notrace2/videos/480p60/sections" &
process_json "sync_notrace3/videos/480p60/sections" &
process_json "sync_notrace4/videos/480p60/sections" 
