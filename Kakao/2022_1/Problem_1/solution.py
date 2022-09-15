def solution(id_list, report, k):
    answer = []
    report_ind = {}
    mail_num = {}
    report_num = {}

    for i in id_list:
        report_ind[i] = set()
        mail_num[i] = 0
        report_num[i] = 0

    for i in report:
        name = i.split(" ")
        if name[1] not in report_ind[name[0]]:
            report_num[name[1]]+=1
            report_ind[name[0]].add(name[1])

    for i in id_list:
        if report_num[i]>=k:
            for key, value in report_ind.items():
                if i in value:
                    mail_num[key]+=1

    return list(mail_num.values())