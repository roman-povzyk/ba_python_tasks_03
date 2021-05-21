phone_number = '0951291264'

if phone_number.isdigit() and len(phone_number) == 10:
    print(f'Дякуємо, у вашому номері 10 цифр, все вірно.')
elif not phone_number.isdigit():
    print(f'У вашому номері є нецифрові символи. Перевірте його ще раз.')

if len(phone_number) != 10:
    print(f'У вашому номері знаків не 10, а {len(phone_number)}. Перевірте його ще раз.')
