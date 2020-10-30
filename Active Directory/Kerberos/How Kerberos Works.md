# How does Kerberos work?

[ **NOTE:** All diagrams from the [Tarlogic's article](https://www.tarlogic.com/en/blog/how-kerberos-works/) that I had mentioned in the README.md ]

#### The whole process:

![Whole Process](https://www.tarlogic.com/wp-content/uploads/2019/01/kerberos_message_summary.png)

#### Flowchart:
1. Request for TGT:
![Request for TGT](https://www.tarlogic.com/wp-content/uploads/2019/03/KRB_AS_REQ.png)
2. Response TGT
![Response TGT](https://www.tarlogic.com/wp-content/uploads/2019/02/KRB_AS_REP.png)
3. Request for TGS
![Request for TGS](https://www.tarlogic.com/wp-content/uploads/2019/02/KRB_TGS_REQ-1.png)
4. Response for TGS
![Response for TGS](https://www.tarlogic.com/wp-content/uploads/2019/02/KRB_TGS_REP.png)
5. Request for Service
![Request for Service](https://www.tarlogic.com/wp-content/uploads/2019/02/KRB_AP_REQ.png)

After that, if user privileges are rigth, this can access to service. If is the case, which not usually happens, the AP will verify the PAC against the KDC. And also, if mutual authentication is needed it will respond to user with a KRB_AP_REP message.
