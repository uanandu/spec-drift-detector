import json, sys, re

def main():
    event = json.load(sys.stdin)
    # Last message from the assistant
    message = event.get("last_assistant_message", "")
    
    has_bullets = bool(re.search(r"^\s*[-*]\s", message, re.MULTILINE))
    has_numbered = bool(re.search(r"^\s*\d+[.)]\s",
 message, re.MULTILINE))
    
    if has_bullets or has_numbered:
        list_kind = "bullet-point" if has_bullets else "numbered"
        sys.stderr.write(
            "DRIFT DETECTED: invariants.md says never format a prose reply "
            f"as a {list_kind} list, but the last response used one."
        )
        sys.exit(2) #exits with 2
        
    sys.exit(0) # exit with 0
    
if __name__ == "__main__":
    main()