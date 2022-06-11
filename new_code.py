import requests
import csv
from datetime import date
import pandas as pd

def extractdata():

    with open('new.csv', 'w') as f:
        writer = csv.writer(f)
        head=['symbol','oi call','strike price','oi put','strike price']
        writer.writerow(head)
        
        
        #this is data for specific month this will change every month so put the latest data
        equities='AARTIIND,ABB,ABBOTINDIA,ABCAPITAL,ABFRL,ACC,ADANIENT,ADANIPORTS,ALKEM,AMARAJABAT,AMBUJACEM,APLLTD,APOLLOHOSP,APOLLOTYRE,ASHOKLEY,ASIANPAINT,ASTRAL,ATUL,AUBANK,AUROPHARMA,AXISBANK,BAJAJ-AUTO,BAJAJFINSV,BAJFINANCE,BALKRISIND,BALRAMCHIN,BANDHANBNK,BANKBARODA,BATAINDIA,BEL,BERGEPAINT,BHARATFORG,BHARTIARTL,BHEL,BIOCON,BOSCHLTD,BPCL,BRITANNIA,BSOFT,CANBK,CANFINHOME,CHAMBLFERT,CHOLAFIN,CIPLA,COALINDIA,COFORGE,COLPAL,CONCOR,COROMANDEL,CROMPTON,CUB,CUMMINSIND,DABUR,DALBHARAT,DEEPAKNTR,DELTACORP,DIVISLAB,DIXON,DLF,DRREDDY,EICHERMOT,ESCORTS,EXIDEIND,FEDERALBNK,FSL,GAIL,GLENMARK,GMRINFRA,GNFC,GODREJCP,GODREJPROP,GRANULES,GRASIM,GSPL,GUJGASLTD,HAL,HAVELLS,HCLTECH,HDFC,HDFCAMC,HDFCBANK,HDFCLIFE,HEROMOTOCO,HINDALCO,HINDCOPPER,HINDPETRO,HINDUNILVR,HONAUT,IBULHSGFIN,ICICIBANK,ICICIGI,ICICIPRULI,IDEA,IDFC,IDFCFIRSTB,IEX,IGL,INDHOTEL,INDIACEM,INDIAMART,INDIGO,INDUSINDBK,INDUSTOWER,INFY,INTELLECT,IOC,IPCALAB,IRCTC,ITC,JINDALSTEL,JKCEMENT,JSWSTEEL,JUBLFOOD,KOTAKBANK,L%26TFH,LALPATHLAB,LAURUSLABS,LICHSGFIN,LT,LTI,LTTS,LUPIN,M%26M,M%26MFIN,MANAPPURAM,MARICO,MARUTI,MCDOWELL-N,MCX,METROPOLIS,MFSL,MGL,MINDTREE,MOTHERSUMI,MPHASIS,MRF,MUTHOOTFIN,NAM-INDIA,NATIONALUM,NAUKRI,NAVINFLUOR,NBCC,NESTLEIND,NMDC,NTPC,OBEROIRLTY,OFSS,ONGC,PAGEIND,PEL,PERSISTENT,PETRONET,PFC,PIDILITIND,PIIND,PNB,POLYCAB,POWERGRID,PVR,RAIN,RAMCOCEM,RBLBANK,RECLTD,RELIANCE,SAIL,SBICARD,SBILIFE,SBIN,SHREECEM,SIEMENS,SRF,SRTRANSFIN,STAR,SUNPHARMA,SUNTV,SYNGENE,TATACHEM,TATACOMM,TATACONSUM,TATAMOTORS,TATAPOWER,TATASTEEL,TCS,TECHM,TITAN,TORNTPHARM,TORNTPOWER,TRENT,TVSMOTOR,UBL,ULTRACEMCO,UPL,VEDL,VOLTAS,WHIRLPOOL,WIPRO,ZEEL,ZYDUSLIFE'
        eques=equities.split(',')
        count=0
        for equ in eques:
            try:
                count+=1
                ogurl='https://www.nseindia.com/api/option-chain-equities?symbol='
                baseurl = "https://www.nseindia.com/"
                url=ogurl+equ
                headers={
                    'user-agent': '!!!goto inspect element and copy from network',
                    'accept-encoding': '!!!goto inspect element and copy from network',
                    'accept-language': '!!!!goto inspect element and copy from network'

                }

                session=requests.Session()
                request=session.get(baseurl, headers=headers, timeout=5)
                cookies=dict(request.cookies)
                response=session.get(url, headers=headers, timeout=5, cookies=cookies)
                rawdata=pd.DataFrame(response.json())
                rawop=pd.DataFrame(rawdata['filtered']['data']).fillna(0)
                print(count)
                
                def dataframe(rawop):
                    data=[]
                    maxc=0
                    maxp=0
                    st1=0
                    st2=0
                    for i in range(0,len(rawop)):
                        calloi=callcoi=cltp=putoi=putcoi=pltp=0
                        stp=rawop['strikePrice'][i]
                        if(rawop['CE'][i]==0):
                            calloi=callcoi=0
                        else:
                            calloi=rawop['CE'][i]['openInterest']
                            callcoi=rawop['CE'][i]['changeinOpenInterest']
                            cltp=rawop['CE'][i]['lastPrice']
                        if(rawop['PE'][i]==0):
                            putoi=putcoi=0
                        else:
                            putoi=rawop['PE'][i]['openInterest']
                            putcoi=rawop['PE'][i]['changeinOpenInterest']
                            pltp=rawop['PE'][i]['lastPrice'] 
                            
                        opdata={
                            'COI':calloi,'CCOI':callcoi,'CLTP':cltp,'SP':stp,
                            'POI':putoi,'PCOI':putcoi,'PLTP':pltp
                        }    
                        if(opdata['COI']>maxc):
                            st1=opdata['SP']
                            maxc=opdata['COI']   
                        if(opdata['POI']>maxp):
                            st2=opdata['SP']
                            maxp=opdata['POI']
                        
                        data.append(opdata)
                    optionchain=pd.DataFrame(data)
                    print(equ.replace("%26","&"),maxc,st1,maxp,st2)
                    xldata=[equ.replace("%26","&"),maxc,st1,maxp,st2]
                    writer.writerow(xldata)
                    return optionchain


                dataframe(rawop)
                
            except:
                continue

def removeemptyrow():
    try:
        print("removing empty")
        today=date.today()
        d=today.strftime("%d_%m_%Y")
        stringfile='new'+d+'oianalysis.csv'
        with open('new.csv', newline='') as in_file:
            with open(stringfile, 'w', newline='') as out_file:
                writer = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writer.writerow(row)
    except:
        print("not removeable row")


extractdata()
removeemptyrow()
print('--------- end ----------')