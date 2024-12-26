def run_challenge():
    tea_type = int(input())
    if tea_type <= 0 or tea_type >= 5:
        return

    reply_provided_by_tea_tasters_lst = list(map(int,input().split()))
    if len(reply_provided_by_tea_tasters_lst) != 5:
        return

    correct_reply = 0
    for reply in reply_provided_by_tea_tasters_lst:
        if reply == tea_type:
            correct_reply += 1


    print(correct_reply)

if __name__ == '__main__':
    run_challenge()