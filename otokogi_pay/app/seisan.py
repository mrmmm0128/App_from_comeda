def seisan(pay_dict):
    people = len(pay_dict)
    sum_pay = sum(pay_dict.values())

    a_pay = sum_pay/people

    new_pay = {key:value-a_pay for key,value in pay_dict.items()}

    conceqence = []

    while True:
        pay = min(new_pay.values())
        pay_people =  [key for key, value in new_pay.items() if value == pay]

        get = max(new_pay.values())
        get_people = [key for key, value in new_pay.items() if value == get]

        payment = min(get,abs(pay))

        for i in range(min(len(pay_people),len(get_people))):
            new_pay[pay_people[i]] += payment
            new_pay[get_people[i]] -= payment
            concequence.append(pay_people[i]+"が"+get_people[i]+"に支払い："+str(round(payment)))
        
        if all(math.isclose(value, 0, abs_tol=1e-9)  for value in new_pay.values()):
            return concequence
            break

