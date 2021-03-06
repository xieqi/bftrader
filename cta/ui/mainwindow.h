#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QCloseEvent>
#include <QMainWindow>
#include <QSystemTrayIcon>

namespace Ui {
class MainWindow;
}

class Profile;
class RobotForm;
class GatewayForm;
class ModelForm;
class PositionForm;
class InfoForm;
class DebugForm;
class ErrorForm;
class WorkingOrderForm;

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MainWindow(QWidget* parent = 0);
    ~MainWindow();
    void init();
    void shutdown();

public slots:

private slots:
    void onTrayIconActivated(QSystemTrayIcon::ActivationReason reason);
    void on_actionAppQuit_triggered();
    void on_actionAppVersion_triggered();
    void on_actionCrashPureCallCrash_triggered();
    void on_actionCrashInvalidParamCrash_triggered();
    void on_actionCrashDerefZeroCrash_triggered();
    void on_actionCrashQFatal_triggered();
    void on_actionCrashdebugbreak_triggered();
    void on_actionCrashDebugBreak_triggered();
    void on_actionCrashExit_triggered();
    void on_actionCrashExitProcess_triggered();
    void on_actionCrashTerminateProcess_triggered();
    void on_actionNetStart_triggered();
    void on_actionNetStop_triggered();
    void on_actionRobotAdd_triggered();
    void on_actionGatewayAdd_triggered();
    void on_actionModelAdd_triggered();

private:
    void closeEvent(QCloseEvent* event) override;
    void createTrayIcon();
    void createActions();
    Profile* profile();

private:
    Ui::MainWindow* ui;

private:
    QAction* minimizeAction;
    QAction* maximizeAction;
    QAction* restoreAction;
    QAction* quitAction;

    QSystemTrayIcon* trayIcon;
    QMenu* trayIconMenu;
    QIcon icon_;

    //tabs
    RobotForm* robotForm_;
    GatewayForm* gatewayForm_;
    ModelForm* modelForm_;
    PositionForm* positionForm_;
    InfoForm* infoForm_;
    DebugForm* debugForm_;
    ErrorForm* errorForm_;
    WorkingOrderForm* workingOrderForm_;
};

#endif // MAINWINDOW_H
